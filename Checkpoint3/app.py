import os
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import networkx as nx
from typing import Optional
import plotly.express as px
import plotly.figure_factory as ff
import scipy.cluster.hierarchy as sch
from sklearn.preprocessing import StandardScaler

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
TREEMAP_PNG = os.path.join(FIG_DIR, "viz_treemap_multi_level.png")
SUNBURST_PNG = os.path.join(FIG_DIR, "viz_sunburst_multi_level.png")
# Fallback paths for older notebook versions
TREEMAP_PNG_OLD = os.path.join(FIG_DIR, "viz_treemap_squarify.png")
DONUT_PNG_OLD = os.path.join(FIG_DIR, "viz_donut_approximation.png")

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

@st.cache_data(show_spinner=False)
def generate_hierarchy_treemap(clean_df: pd.DataFrame) -> Optional[pd.DataFrame]:
    """Generate hierarchy_treemap.csv dynamically from clean_df if it doesn't exist."""
    if clean_df is None or len(clean_df) == 0:
        return None
    try:
        def size_group(size):
            if size >= 15:
                return "Big (>=15 people)"
            elif size >= 8:
                return "Medium (8-14 people)"
            else:
                return "Small (3-7 people)"
        
        df = clean_df.copy()
        df["size_group"] = df["size_cleaned"].apply(size_group)
        df["Root"] = "YouTube_Communities"
        hierarchy_df = df.groupby(["Root", "size_group", "community_id"])["size_cleaned"].sum().reset_index(name="members_count")
        return hierarchy_df
    except Exception:
        return None

@st.cache_data(show_spinner=False)
def generate_interactive_dendrogram(nodes_df: pd.DataFrame, sample_size: int = 30):
    """Generate interactive dendrogram using Plotly with full display and zoom capabilities."""
    if nodes_df is None or len(nodes_df) == 0:
        return None
    try:
        sample_df = nodes_df.sample(n=min(sample_size, len(nodes_df)), random_state=1)
        scaler = StandardScaler()
        sample_scaled = scaler.fit_transform(sample_df[['degree', 'weighted_degree']])
        
        # Create interactive dendrogram with Plotly
        fig = ff.create_dendrogram(
            sample_scaled,
            orientation='bottom',
            labels=sample_df['node'].astype(str).tolist(),
            linkagefun=lambda x: sch.linkage(x, method='ward')
        )
        
        # Update layout for better display and interactivity
        fig.update_layout(
            title=dict(
                text=' Dendrograma de Clustering Jerárquico (Interactive)',
                x=0.5,
                xanchor='center',
                font=dict(size=16)
            ),
            xaxis=dict(
                title='Nodos (ID)',
                tickangle=-45,
                tickfont=dict(size=9),
                showgrid=True,
                gridcolor='lightgray',
                automargin=True
            ),
            yaxis=dict(
                title='Distancia (Ward)',
                showgrid=True,
                gridcolor='lightgray',
                automargin=True
            ),
            height=900,
            autosize=True,
            margin=dict(l=80, r=50, t=120, b=180),
            hovermode='closest',
            plot_bgcolor='white',
            paper_bgcolor='white'
        )
        
        # Enable zoom and pan interactions
        fig.update_xaxes(fixedrange=False)
        fig.update_yaxes(fixedrange=False)
        
        return fig
    except Exception as e:
        st.error(f"Error generating dendrogram: {e}")
        return None

@st.cache_data(show_spinner=False)
def generate_interactive_treemap(hierarchy_df: pd.DataFrame):
    """Generate interactive treemap using Plotly."""
    if hierarchy_df is None or len(hierarchy_df) == 0:
        return None
    try:
        treemap_data = hierarchy_df.groupby(['Root', 'size_group']).agg({'members_count': 'sum'}).reset_index()
        
        fig = px.treemap(
            treemap_data,
            path=[px.Constant("YouTube Communities"), 'Root', 'size_group'],
            values='members_count',
            color='members_count',
            color_continuous_scale='Blues',
            title='Treemap de Comunidades por Tamaño (Interactive)'
        )
        
        fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))
        return fig
    except Exception as e:
        st.error(f"Error generating treemap: {e}")
        return None

@st.cache_data(show_spinner=False)
def generate_interactive_sunburst(hierarchy_df: pd.DataFrame):
    """Generate interactive sunburst using Plotly with percentages."""
    if hierarchy_df is None or len(hierarchy_df) == 0:
        return None
    try:
        sunburst_data = hierarchy_df.groupby(['Root', 'size_group']).agg({'members_count': 'sum'}).reset_index()
        
        fig = px.sunburst(
            sunburst_data,
            path=['Root', 'size_group'],
            values='members_count',
            color='members_count',
            color_continuous_scale='Blues',
            title='Sunburst de Comunidades por Tamaño (Interactive)'
        )
        
        fig.update_traces(
            texttemplate='%{label}<br>%{percentEntry:.1%}',
            textinfo='label+percent entry',
            hovertemplate='<b>%{label}</b><br>Miembros: %{value:,.0f}<br>Porcentaje del total: %{percentEntry:.1%}<extra></extra>'
        )
        
        fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))
        return fig
    except Exception as e:
        st.error(f"Error generating sunburst: {e}")
        return None

# --- Sidebar: Simple vs Advanced ---
st.sidebar.header("Display mode")
simple_mode = st.sidebar.toggle("Simple mode (recommended)", value=True, help="Focused view with KPIs and community visualizations. Switch off for advanced overview.")

# --- Load Data ---
clean_df = load_csv(CLEAN_NO_OUT)
edges_df = load_csv(EDGES_CSV)
nodes_df = load_csv(NODES_CSV)
# Try to load hierarchy_treemap, if not found generate it dynamically from clean_df
hier_df = load_csv(HIER_TREEMAP)
if hier_df is None and clean_df is not None:
    hier_df = generate_hierarchy_treemap(clean_df)

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
        st.info("Run the notebook first to generate files in data/processed.")
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
        st.markdown("The chart highlights the **top contacts by connection strength** — the ones who **amplify Ana Sofía Mendoza's reach** across her professional network.")

    st.markdown("---")
    st.subheader(" Network focus")
    st.write("We focus on the people who amplify the most. You choose whom to contact first; we rank them by potential impact.")

# --- Advanced Mode (for analysts/managers) ---
else:
    overview_tab, visualizations_tab, method_tab = st.tabs([
        "Overview", "Visualizations (Section 7)", "Methodology"
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
        st.markdown(
            """
            ## Network Insights: Community Size Distribution

    
            ### Why It Matters
            For digital marketing professionals like **Ana Sofía Mendoza**, this insight reveals that:
            - Most engagement happens within **microcommunities**.  
            - **Personalized campaigns** and **micro-influencer strategies** can achieve higher conversion rates.  
            - Large-scale messages are **less effective** in a fragmented network.

            ### Strategic Application
            - Focus ad spend on **smaller, high-interaction clusters**.  
            - Identify **connectors** within medium groups (8–14 members) to expand organically.  
            - Use data analytics to replicate the growth patterns of the **16% large communities**.

            ### Impact
            Understanding community size enables **better audience segmentation**, **optimized paid media**, and **sustained growth strategies**.
            """
        )

    with visualizations_tab:
        st.subheader("Visualizations from Section 7: Graphs for Streamlit Visualization")
        st.markdown("These visualizations provide strategic insights into the network structure and community distribution.")
        
        st.markdown("---")
        st.markdown("### 1. Dendrograma de Clustering Jerárquico")
        dendro_fig = generate_interactive_dendrogram(nodes_df, sample_size=30)
        if dendro_fig is not None:
            st.plotly_chart(
                dendro_fig, 
                config={
                    'displayModeBar': True,
                    'modeBarButtonsToAdd': ['zoom2d', 'pan2d', 'select2d', 'lasso2d', 'zoomIn2d', 'zoomOut2d', 'autoScale2d', 'resetScale2d'],
                    'displaylogo': False
                },
                use_container_width=True
            )
            st.markdown("""
            **Purpose:** Identifies natural clusters of nodes based on similarity in degree and weighted_degree.
            
            **About the chart:**
            - Nodes that merge at lower distances are more similar
            - Long vertical lines indicate distinct groups
            - Use this to identify natural audience segments for personalized campaigns
            
            
            """)
        else:
            st.info("Dendrogram not available. Ensure nodes_df is loaded from the notebook (Section 7).")
        
        st.markdown("---")
        st.markdown("### 2. Treemap de Comunidades por Tamaño")
        c1, c2 = st.columns(2)
        with c1:
            treemap_fig = generate_interactive_treemap(hier_df)
            if treemap_fig is not None:
                st.plotly_chart(
                    treemap_fig, 
                    config={
                        'displayModeBar': True,
                        'modeBarButtonsToAdd': ['zoom2d', 'pan2d', 'select2d', 'lasso2d', 'zoomIn2d', 'zoomOut2d', 'autoScale2d', 'resetScale2d'],
                        'displaylogo': False
                    },
                    use_container_width=True
                )
            else:
                st.info("Treemap not available. Ensure hierarchy_treemap.csv is loaded or clean_no_outliers.csv exists.")
        with c2:
            st.markdown("""
            **Purpose:** Shows the absolute distribution of members across community size categories.
            
            **About the chart**
            - Each rectangle represents communities grouped by size
            - Larger rectangles = more members in that category
           
            
            **Strategic insight:**
            - **Small communities (3-7)**: Ideal for personalized engagement and deep relationships
            - **Medium communities (8-14)**: Balance between personalization and reach
            - **Large communities (≥15)**: Perfect for mass campaigns and broad reach
            
            **Use case:** Optimize resource allocation based on absolute member concentration
            """)
        
        st.markdown("---")
        st.markdown("### 3. Sunburst de Comunidades por Tamaño")
        sunburst_fig = generate_interactive_sunburst(hier_df)
        if sunburst_fig is not None:
            st.plotly_chart(
                sunburst_fig, 
                config={
                    'displayModeBar': True,
                    'modeBarButtonsToAdd': ['zoom2d', 'pan2d', 'select2d', 'lasso2d', 'zoomIn2d', 'zoomOut2d', 'autoScale2d', 'resetScale2d'],
                    'displaylogo': False
                },
                use_container_width=True
            )
            st.markdown("""
            **Purpose:** Shows the proportional distribution of members across community size categories.
            
            **About the chart:**
            - Center represents total YouTube Communities
            - Outer rings show size categories with percentages
            - Each segment shows the proportion of total members
            
            
            **Strategic application:**
            - Use percentages to allocate marketing resources effectively
            - Understand the relative distribution of your audience
            - Balance tactics between small, medium, and large communities
            
            **Use case:** Make strategic decisions based on proportional distribution rather than absolute numbers
            """)
        else:
            st.info("Sunburst chart not available. Ensure hierarchy_treemap.csv is loaded or clean_no_outliers.csv exists.")
        
        st.markdown("---")
        st.markdown("### Combined Strategic Value")
        st.markdown("""
        These three visualizations work together to provide a comprehensive understanding:
        
        - **Dendrogram**: Identifies *natural groupings* based on similarity
        - **Treemap**: Shows *absolute volume* and member concentration
        - **Sunburst**: Displays *proportional distribution* with percentages
        
        Together, they enable data-driven decisions for audience segmentation, resource allocation, and strategic marketing campaigns.
        """)

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
