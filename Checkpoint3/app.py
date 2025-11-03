import os
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import networkx as nx
from typing import Optional

# --- Theme tweaks for friendlier visuals ---
st.set_page_config(page_title="Network Influence Dashboard", layout="wide")
PRIMARY = "#4ECDC4"
ACCENT = "#FFE66D"

# --- Paths (aligned with the notebook) ---
ROOT = "/content" if os.path.exists("/content") else os.getcwd()
PROC_DIR = os.path.join(ROOT, "data", "processed")
FIG_DIR = os.path.join(ROOT, "reports", "figures")

CLEAN_NO_OUT = os.path.join(PROC_DIR, "youtube_clean_no_outliers.csv")
EDGES_CSV = os.path.join(PROC_DIR, "youtube_edges.csv")
NODES_CSV = os.path.join(PROC_DIR, "youtube_nodes.csv")
LINKAGE_NPY = os.path.join(PROC_DIR, "linkage_matrix.npy")
NODE_LABELS = os.path.join(PROC_DIR, "dendrogram_node_labels.csv")
HIER_TREEMAP = os.path.join(PROC_DIR, "hierarchy_treemap.csv")

DENDRO_PNG = os.path.join(FIG_DIR, "viz_dendrogram.png")
TREEMAP_PNG = os.path.join(FIG_DIR, "viz_treemap_squarify.png")
DONUT_PNG = os.path.join(FIG_DIR, "viz_donut_approximation.png")

st.title("Network Performance Dashboard")
st.caption("We identify the key people who amplify your reach and prioritize simple, high‑impact actions.")

# --- Utilities ---
@st.cache_data(show_spinner=False)
def load_csv(path: str) -> Optional[pd.DataFrame]:
    try:
        return pd.read_csv(path)
    except Exception:
        return None

@st.cache_data(show_spinner=False)
def load_numpy(path: str) -> Optional[np.ndarray]:
    try:
        return np.load(path)
    except Exception:
        return None

@st.cache_data(show_spinner=False)
def build_graph(edges_df: pd.DataFrame) -> Optional[nx.Graph]:
    try:
        return nx.from_pandas_edgelist(edges_df, "source", "target", edge_attr="weight")
    except Exception:
        return None

# --- Sidebar: Simple vs Advanced ---
st.sidebar.header("Display mode")
simple_mode = st.sidebar.toggle("Simple mode (recommended)", value=True, help="KPI and action‑focused view. Switch off to see the network and advanced controls.")

# Basic filters (kept simple)
min_edge_weight = 3
show_top_n = 20

# Advanced controls (hidden in simple mode)
use_pagerank = False
use_betweenness = False
k_sample = 300
w_wdeg = 0.5
w_pr = 0.3
w_bw = 0.2

if not simple_mode:
    st.sidebar.subheader("Network filters")
    min_edge_weight = st.sidebar.slider("Minimum edge weight", 1, 50, 3, 1)
    show_top_n = st.sidebar.slider("Top N nodes by influence", 10, 300, 80, 10)

    st.sidebar.subheader("Centralities (optional)")
    use_pagerank = st.sidebar.checkbox("Compute PageRank", value=False)
    use_betweenness = st.sidebar.checkbox("Compute Betweenness (approx.)", value=False)
    if use_betweenness:
        k_sample = st.sidebar.slider("Betweenness sampling (k)", 50, 1500, 400, 50)

    st.sidebar.subheader("Score weighting")
    w_wdeg = st.sidebar.slider("Weighted_degree weight", 0.0, 1.0, 0.6, 0.05)
    w_pr = st.sidebar.slider("PageRank weight", 0.0, 1.0, 0.25, 0.05)
    w_bw = st.sidebar.slider("Betweenness weight", 0.0, 1.0, 0.15, 0.05)
    s = max(w_wdeg + w_pr + w_bw, 1e-9)
    w_wdeg, w_pr, w_bw = w_wdeg / s, w_pr / s, w_bw / s

# --- Load Data ---
clean_df = load_csv(CLEAN_NO_OUT)
edges_df = load_csv(EDGES_CSV)
nodes_df = load_csv(NODES_CSV)
hier_df = load_csv(HIER_TREEMAP)

# --- Simple Mode (digestible, story-first) ---
if simple_mode:
    # KPIs amigables
    st.subheader(" What matters")
    total_nodes = len(nodes_df) if nodes_df is not None else 0
    total_edges = len(edges_df) if edges_df is not None else 0
    total_coms = len(clean_df) if clean_df is not None else 0

    c1, c2, c3 = st.columns(3)
    c1.metric("People in the YouTube network", f"{total_nodes:,}")
    c2.metric("Detected connections", f"{total_edges:,}")
    c3.metric("Mapped communities", f"{total_coms:,}")

    st.markdown("---")
    st.subheader(" Contacts that amplify your reach")
    if nodes_df is None or len(nodes_df) == 0:
        st.info("Ejecuta primero la notebook para generar los archivos en data/processed.")
    else:
        top = nodes_df.sort_values("weighted_degree", ascending=False).head(8)
        # Bar chart simple
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.bar(top["node"].astype(str), top["weighted_degree"], color=PRIMARY)
        ax.set_title("Top amplifiers (by weighted connections)")
        ax.set_ylabel("Connection strength")
        ax.set_xlabel("Contact (ID)")
        ax.set_xticklabels(top["node"].astype(str), rotation=25, ha="right")
        st.pyplot(fig)

        # Mensaje explicativo para el perfil de interés
        st.markdown("The chart highlights the **top contacts by connection strength** — the ones who **amplify Ana Sofía Mendoza’s reach** across her professional network.")

    st.markdown("---")
    st.subheader(" Network focus")
    st.write("We focus on the people who amplify the most. You choose whom to contact first; we rank them by potential impact.")

# --- Advanced Mode (for analysts/managers) ---
else:
    overview_tab, network_tab, hierarchy_tab, reco_tab, method_tab = st.tabs([
        "Overview", "Network & Influence", "Hierarchies & Segments", "Recommendations", "Methodology"
    ])

    with overview_tab:
        st.subheader("Overview")
        total_coms = len(clean_df) if clean_df is not None else 0
        total_edges = len(edges_df) if edges_df is not None else 0
        total_nodes = len(nodes_df) if nodes_df is not None else 0
        density = 0.0
        if edges_df is not None and nodes_df is not None and total_nodes > 1:
            density = (total_edges) / (total_nodes * (total_nodes - 1) / 2)
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Communities (clean)", f"{total_coms:,}")
        c2.metric("Nodes", f"{total_nodes:,}")
        c3.metric("Edges", f"{total_edges:,}")
        c4.metric("Approx. density", f"{density:.4f}")

        st.markdown("---")
        if nodes_df is not None and len(nodes_df) > 0:
            st.subheader("Top nodes by weighted_degree")
            top_nodes_tbl = nodes_df.sort_values("weighted_degree", ascending=False).head(5)[["node", "weighted_degree"]]
            c = st.columns(5)
            for i, (_, r) in enumerate(top_nodes_tbl.iterrows()):
                c[i].metric(label=f"Top {i+1}", value=str(r["node"]), delta=f"wd={int(r['weighted_degree'])}")
            st.markdown("- These contacts are the ones that amplify messages the most due to their weighted connections. They usually provide the highest incremental reach..")
        else:
            st.info("Aún no se han generado los nodos.")

        st.markdown("---")
        c1, c2 = st.columns(2)
        with c1:
            if os.path.exists(TREEMAP_PNG):
                st.image(TREEMAP_PNG, caption="Communities treemap")
            else:
                st.info("Treemap no disponible. Genera las figuras desde la notebook.")
        with c2:
            if os.path.exists(DONUT_PNG):
                st.image(DONUT_PNG, caption="Communities percentage (Donut)")
            else:
                st.info("Donut no disponible. Genera las figuras desde la notebook.")

        # Insight block under Overview visuals
        st.markdown(
            """
            ##  Network Insights: Community Size Distribution

            ###  Key Takeaway
            More than **half of the communities (52%)** in the network are *small groups* (3–7 members).

            ###  Why It Matters
            For digital marketing professionals like **Ana Sofía Mendoza**, this insight reveals that:
            - Most engagement happens within **microcommunities**.  
            - **Personalized campaigns** and **micro-influencer strategies** can achieve higher conversion rates.  
            - Large-scale messages are **less effective** in a fragmented network.

            ###  Strategic Application
            - Focus ad spend on **smaller, high-interaction clusters**.  
            - Identify **connectors** within medium groups (8–14 members) to expand organically.  
            - Use data analytics to replicate the growth patterns of the **16% large communities**.

            ###  Impact
            Understanding community size enables **better audience segmentation**, **optimized paid media**, and **sustained growth strategies**.
            """
        )

    with network_tab:
        st.subheader("Network & Influence")
        if edges_df is None or nodes_df is None:
            st.info("Faltan archivos de aristas/nodos.")
        else:
            filt_edges = edges_df[edges_df["weight"] >= min_edge_weight].copy()
            st.write(f"Edges after filter ≥ {min_edge_weight}: {len(filt_edges):,}")
            top_nodes_list = nodes_df.sort_values("weighted_degree", ascending=False).head(show_top_n)["node"].astype(str).tolist()
            sub_edges = filt_edges[filt_edges["source"].astype(str).isin(top_nodes_list) & filt_edges["target"].astype(str).isin(top_nodes_list)]
            G = build_graph(sub_edges)
            if G is None or G.number_of_nodes() == 0:
                st.warning("No hay subgrafo para los filtros.")
            else:
                pr_dict, bw_dict = {}, {}
                if use_pagerank:
                    try: pr_dict = nx.pagerank(G, weight="weight")
                    except Exception: pr_dict = {}
                if use_betweenness:
                    try: bw_dict = nx.betweenness_centrality(G, k=min(k_sample, G.number_of_nodes()), weight="weight", seed=42)
                    except Exception: bw_dict = {}

                fig, ax = plt.subplots(figsize=(8, 6))
                pos = nx.spring_layout(G, seed=42, k=0.2)
                wd_series = nodes_df.set_index("node")["weighted_degree"] if nodes_df is not None and "node" in nodes_df else pd.Series(dtype=float)
                sizes = []
                for n in G.nodes():
                    key = str(n)
                    val = wd_series.get(key, 0) if key in wd_series.index else 0
                    sizes.append(5 + 0.5 * float(val))
                nx.draw_networkx_edges(G, pos, ax=ax, alpha=0.15)
                nx.draw_networkx_nodes(G, pos, ax=ax, node_size=sizes, node_color=PRIMARY)
                ax.set_title("Subgraph of influential nodes")
                ax.axis("off")
                st.pyplot(fig)

                selected_nodes = nodes_df[nodes_df["node"].astype(str).isin(list(G.nodes()))].copy()
                if use_pagerank: selected_nodes["pagerank"] = selected_nodes["node"].astype(str).map(pr_dict).fillna(0)
                if use_betweenness: selected_nodes["betweenness"] = selected_nodes["node"].astype(str).map(bw_dict).fillna(0)
                st.markdown("- Larger nodes are hubs: collaborating with them spreads messages faster.\n- Adjust the weight filter to remove noise and keep strong relationships.")

    with hierarchy_tab:
        st.subheader("Hierarchies & Segments")
        c1, c2 = st.columns(2)
        with c1:
            if os.path.exists(DENDRO_PNG):
                st.image(DENDRO_PNG, caption="Dendrogram — similarity among top nodes")
            else:
                st.info("Dendrograma no disponible. Genera la matriz de linkage desde la notebook.")
        with c2:
            if hier_df is not None and len(hier_df) > 0:
                st.markdown("**How to read it:** The treemap groups communities by size (Small/Medium/Large).\n- Use it to balance tactics: personalized messages in small groups and scalable content in larger ones.")
            else:
                st.info("Jerarquía Treemap no disponible. Ejecuta la notebook para crear hierarchy_treemap.csv.")

    with reco_tab:
        st.subheader("Connection recommendations")
        if nodes_df is None or len(nodes_df) == 0:
            st.info("No hay nodos para recomendar.")
        else:
            df_score = nodes_df.copy()
            def norm_col(s: pd.Series) -> pd.Series:
                if s is None or len(s) == 0: return pd.Series(np.zeros(0))
                s = s.fillna(0).astype(float)
                rng = s.max() - s.min()
                return (s - s.min()) / rng if rng > 0 else s * 0
            pr_full, bw_full = None, None
            if use_pagerank and edges_df is not None:
                try:
                    G_full = build_graph(edges_df)
                    pr_full = nx.pagerank(G_full, weight="weight") if G_full is not None else {}
                    df_score["pagerank"] = df_score["node"].astype(str).map(pr_full).fillna(0)
                except Exception:
                    df_score["pagerank"] = 0.0
            if use_betweenness and edges_df is not None:
                try:
                    G_full = build_graph(edges_df)
                    k_eff = min(500, G_full.number_of_nodes()) if G_full is not None else 0
                    bw_full = nx.betweenness_centrality(G_full, k=k_eff, weight="weight", seed=42) if G_full is not None else {}
                    df_score["betweenness"] = df_score["node"].astype(str).map(bw_full).fillna(0)
                except Exception:
                    df_score["betweenness"] = 0.0
            df_score["wd_norm"] = norm_col(df_score.get("weighted_degree", pd.Series(dtype=float)))
            df_score["pr_norm"] = norm_col(df_score.get("pagerank", pd.Series(dtype=float))) if use_pagerank else 0.0
            df_score["bw_norm"] = norm_col(df_score.get("betweenness", pd.Series(dtype=float))) if use_betweenness else 0.0
            s = max(w_wdeg + w_pr + w_bw, 1e-9)
            w_wdeg_n, w_pr_n, w_bw_n = w_wdeg / s, w_pr / s, w_bw / s
            df_score["reco_score"] = w_wdeg_n * df_score["wd_norm"] + w_pr_n * df_score["pr_norm"] + w_bw_n * df_score["bw_norm"]

            top_n = st.slider("Number of recommendations", 5, 50, 12, 3)
            rec_cols = ["node", "degree", "weighted_degree", "reco_score"]
            if use_pagerank: rec_cols.insert(3, "pagerank")
            if use_betweenness: rec_cols.insert(3 if use_pagerank else 3, "betweenness")
            rec = df_score.sort_values("reco_score", ascending=False).head(top_n)[rec_cols].rename(columns={"node": "candidate_node"})
            st.markdown(f"Suggested **{len(rec)}** contacts prioritized by potential impact. Download the CSV for outreach.")
            st.download_button("Download recommendations (CSV)", rec.to_csv(index=False).encode("utf-8"), file_name="influence_recommendations.csv", mime="text/csv")

    with method_tab:
        st.subheader("Resources")
        st.markdown("- Source: SNAP (YouTube with communities). Cleaning, relational projection and centrality metrics.")
        st.caption("Switch off Simple Mode to view the network and advanced controls.")

        st.markdown("---")
        st.subheader("Glossary (what it means and why it matters)")
        st.markdown(
            """
            - **SNAP**: Stanford Network Analysis Project. Real‑world network datasets used to analyze connections and communities.
            - **Graph**: the network representation made of nodes and edges.
            - **Node**: a person/account in the network. It matters because messages start or reach here.
            - **Edge**: connection between two nodes. In this project it’s created when two users co‑belong to communities; its **weight** is how many times they co‑appear (higher weight = stronger tie).
            - **Subgraph**: a portion of the graph (e.g., only the most influential nodes). Useful to focus and reduce noise.
            - **Degree**: number of direct connections of a node. High degree = good initial diffusion.
            - **Weighted_degree (wd)**: degree weighted by tie strength. Higher wd = greater real amplification capacity. It’s the main metric to prioritize contacts.
            - **Connection strength**: term used in Simple Mode; it corresponds to weighted_degree. It indicates how strongly a contact can amplify messages in the network. Higher strength = higher potential reach.
            - **Approx. density**: how connected the network is (0 to 1). Low density suggests growing by connecting communities via “bridges”.
            - **PageRank**: global importance of a node considering the importance of its neighbors. Useful for high‑impact strategic alliances.
            - **Betweenness**: measures how much a node acts as a **bridge** across groups. High betweenness = entry point to new segments.
            - **Score weighting**: weights combining wd, PageRank and Betweenness to rank recommendations. Lets you emphasize reach (wd), authority (PageRank) or access to new segments (Betweenness).
            """
        )
