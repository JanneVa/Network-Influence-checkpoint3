import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import squarify
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.cluster import hierarchy
from scipy.spatial.distance import pdist
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings('ignore')

# Page configuration
st.set_page_config(
    page_title="TCF Strategic Dashboard",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: bold;
    }
    .section-header {
        font-size: 2rem;
        color: #2E8B57;
        margin-top: 2rem;
        margin-bottom: 1rem;
        border-bottom: 2px solid #2E8B57;
        padding-bottom: 0.5rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
        margin: 0.5rem 0;
    }
    .strategy-box {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 0.5rem;
        border: 1px solid #dee2e6;
        margin: 1rem 0;
    }
    .highlight-box {
        background-color: #e3f2fd;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #2196f3;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    try:
        # Load country data
        country_data = pd.read_csv('country_gdp_population.csv')
        
        # Load organizational structure data
        org_data = pd.read_csv('org_structure.csv')
        
        return country_data, org_data
    except FileNotFoundError as e:
        st.error(f"Error loading data: {e}")
        st.info("Please ensure the CSV files are in the same directory as this script.")
        return None, None

def create_treemap(data, title, color_col, size_col):
    """Create an interactive treemap"""
    fig = px.treemap(
        data, 
        path=['continent', 'country'], 
        values=size_col,
        color=color_col,
        title=title,
        color_continuous_scale='Viridis'
    )
    fig.update_layout(
        title_font_size=16,
        font_size=12,
        margin=dict(t=50, l=0, r=0, b=0)
    )
    return fig

def create_sunburst(data, title, color_col, size_col):
    """Create an interactive sunburst chart"""
    fig = px.sunburst(
        data, 
        path=['continent', 'country'], 
        values=size_col,
        color=color_col,
        title=title,
        color_continuous_scale='Viridis'
    )
    fig.update_layout(
        title_font_size=16,
        font_size=12,
        margin=dict(t=50, l=0, r=0, b=0)
    )
    return fig

def create_dendrogram(data, title):
    """Create a hierarchical dendrogram"""
    # Prepare data for clustering
    numeric_data = data[['population', 'gdp_per_capita']].copy()
    numeric_data = numeric_data.fillna(numeric_data.mean())
    
    # Standardize the data
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(numeric_data)
    
    # Perform hierarchical clustering
    linkage_matrix = linkage(scaled_data, method='ward')
    
    # Create dendrogram
    fig, ax = plt.subplots(figsize=(12, 8))
    dendrogram(linkage_matrix, labels=data['country'].values, ax=ax, leaf_rotation=90)
    ax.set_title(title, fontsize=16, fontweight='bold')
    ax.set_xlabel('Countries', fontsize=12)
    ax.set_ylabel('Distance', fontsize=12)
    plt.tight_layout()
    
    return fig

def create_org_treemap(data, title):
    """Create organizational structure treemap"""
    fig = px.treemap(
        data, 
        path=['parent', 'label'], 
        values='value',
        title=title,
        color='value',
        color_continuous_scale='Blues'
    )
    fig.update_layout(
        title_font_size=16,
        font_size=12,
        margin=dict(t=50, l=0, r=0, b=0)
    )
    return fig

def main():
    # Header
    st.markdown('<h1 class="main-header">TCF Strategic Dashboard</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; font-size: 1.2rem; color: #666;">Strategic Analysis for Terra Cotta Foods Expansion</p>', unsafe_allow_html=True)
    
    # Load data
    country_data, org_data = load_data()
    
    if country_data is None or org_data is None:
        st.stop()
    
    # Sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox(
        "Select Analysis",
        ["Executive Summary", "Hierarchical Analysis", "Strategic Recommendations"]
    )
    
    if page == "Executive Summary":
        show_executive_summary(country_data, org_data)
    elif page == "Hierarchical Analysis":
        show_hierarchical_analysis(country_data, org_data)
    elif page == "Strategic Recommendations":
        show_strategic_recommendations(country_data, org_data)

def show_executive_summary(country_data, org_data):
    st.markdown('<h2 class="section-header">Executive Summary</h2>', unsafe_allow_html=True)
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Total Countries Analyzed",
            value=len(country_data),
            delta="12 priority markets"
        )
    
    with col2:
        total_population = country_data['population'].sum() / 1e9
        st.metric(
            label="Total Population (Billions)",
            value=f"{total_population:.2f}B",
            delta="Global coverage"
        )
    
    with col3:
        total_gdp = country_data['gdp_total'].sum() / 1e12
        st.metric(
            label="Total GDP (Trillions)",
            value=f"${total_gdp:.2f}T",
            delta="Market opportunity"
        )
    
    with col4:
        avg_gdp_per_capita = country_data['gdp_per_capita'].mean()
        st.metric(
            label="Average GDP per Capita",
            value=f"${avg_gdp_per_capita:,.0f}",
            delta="Purchasing power"
        )
    
    # Key strategic decisions
    st.markdown('<h3 class="section-header">Key Strategic Decisions</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="strategy-box">
        <h4>Latin America Strategy</h4>
        <ul>
        <li>Focus on premium products</li>
        <li>Target countries: Brazil, Mexico, Argentina, Chile</li>
        <li>Establish distribution centers in major cities</li>
        <li>Leverage growing middle class</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="strategy-box">
        <h4>Asia Strategy</h4>
        <ul>
        <li>Focus on volume products</li>
        <li>Target countries: China, India, Indonesia, Vietnam</li>
        <li>Multiple distribution centers for coverage</li>
        <li>Scale operations for mass market</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Market opportunity chart
    st.markdown('<h3 class="section-header">Market Opportunity Analysis</h3>', unsafe_allow_html=True)
    
    # Create scatter plot
    fig = px.scatter(
        country_data, 
        x='population', 
        y='gdp_per_capita',
        size='gdp_total',
        color='continent',
        hover_data=['country'],
        title='Market Opportunity by Country',
        labels={
            'population': 'Population',
            'gdp_per_capita': 'GDP per Capita (USD)',
            'continent': 'Continent'
        }
    )
    fig.update_layout(
        title_font_size=16,
        font_size=12,
        width=800,
        height=500
    )
    st.plotly_chart(fig, use_container_width=True)

def show_hierarchical_analysis(country_data, org_data):
    st.markdown('<h2 class="section-header">Hierarchical Analysis</h2>', unsafe_allow_html=True)
    
    # Analysis type selection
    analysis_type = st.selectbox(
        "Select Analysis Type",
        ["Country Analysis", "Organizational Structure"]
    )
    
    if analysis_type == "Country Analysis":
        # Country treemap
        st.markdown('<h3 class="section-header">Country Market Analysis</h3>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            fig1 = create_treemap(
                country_data, 
                "Population Distribution by Country",
                "gdp_per_capita",
                "population"
            )
            st.plotly_chart(fig1, use_container_width=True)
        
        with col2:
            fig2 = create_treemap(
                country_data, 
                "GDP Distribution by Country",
                "population",
                "gdp_total"
            )
            st.plotly_chart(fig2, use_container_width=True)
        
        # Sunburst charts
        st.markdown('<h3 class="section-header">Regional Analysis</h3>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            fig3 = create_sunburst(
                country_data, 
                "Population by Region and Country",
                "gdp_per_capita",
                "population"
            )
            st.plotly_chart(fig3, use_container_width=True)
        
        with col2:
            fig4 = create_sunburst(
                country_data, 
                "GDP by Region and Country",
                "population",
                "gdp_total"
            )
            st.plotly_chart(fig4, use_container_width=True)
        
        # Dendrogram
        st.markdown('<h3 class="section-header">Market Clustering Analysis</h3>', unsafe_allow_html=True)
        fig5 = create_dendrogram(country_data, "Country Clustering Based on Population and GDP per Capita")
        st.pyplot(fig5)
    
    else:
        # Organizational structure analysis
        st.markdown('<h3 class="section-header">Organizational Structure</h3>', unsafe_allow_html=True)
        
        fig = create_org_treemap(org_data, "TCF Organizational Structure")
        st.plotly_chart(fig, use_container_width=True)
        
        # Department analysis
        st.markdown('<h3 class="section-header">Department Analysis</h3>', unsafe_allow_html=True)
        
        # Group by parent department
        dept_summary = org_data.groupby('parent').agg({
            'value': 'sum',
            'label': 'count'
        }).reset_index()
        dept_summary.columns = ['Department', 'Total Budget', 'Number of Sub-departments']
        
        st.dataframe(dept_summary, use_container_width=True)

def show_strategic_recommendations(country_data, org_data):
    st.markdown('<h2 class="section-header">Strategic Recommendations</h2>', unsafe_allow_html=True)
    
    # Priority countries analysis
    st.markdown('<h3 class="section-header">Priority Countries Analysis</h3>', unsafe_allow_html=True)
    
    # Filter priority countries
    priority_countries = country_data[country_data['priority_level'].isin([1, 2])].copy()
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Population analysis
        fig1 = px.bar(
            priority_countries.sort_values('population', ascending=True),
            x='population',
            y='country',
            orientation='h',
            title='Population of Priority Countries',
            color='continent',
            color_discrete_map={'Americas': '#1f77b4', 'Asia': '#ff7f0e'}
        )
        fig1.update_layout(
            title_font_size=16,
            font_size=12,
            height=400
        )
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        # GDP per capita analysis
        fig2 = px.bar(
            priority_countries.sort_values('gdp_per_capita', ascending=True),
            x='gdp_per_capita',
            y='country',
            orientation='h',
            title='GDP per Capita of Priority Countries',
            color='continent',
            color_discrete_map={'Americas': '#1f77b4', 'Asia': '#ff7f0e'}
        )
        fig2.update_layout(
            title_font_size=16,
            font_size=12,
            height=400
        )
        st.plotly_chart(fig2, use_container_width=True)
    
    # Market opportunity scatter plot
    st.markdown('<h3 class="section-header">Market Opportunity Matrix</h3>', unsafe_allow_html=True)
    
    fig3 = px.scatter(
        priority_countries,
        x='population',
        y='gdp_per_capita',
        size='gdp_total',
        color='market_type',
        hover_data=['country', 'priority_level'],
        title='Market Opportunity Matrix - Priority Countries',
        labels={
            'population': 'Population',
            'gdp_per_capita': 'GDP per Capita (USD)',
            'market_type': 'Market Type'
        },
        color_discrete_map={'Premium': '#2E8B57', 'Volume': '#FF6347'}
    )
    fig3.update_layout(
        title_font_size=16,
        font_size=12,
        width=800,
        height=500
    )
    st.plotly_chart(fig3, use_container_width=True)
    
    # Implementation roadmap
    st.markdown('<h3 class="section-header">Implementation Roadmap</h3>', unsafe_allow_html=True)
    
    # Create implementation phases data
    phases_data = pd.DataFrame({
        'Phase': ['Phase 1: Latin America', 'Phase 2: Asia', 'Phase 3: Optimization'],
        'Start_Year': [2024, 2025, 2027],
        'End_Year': [2025, 2027, 2028],
        'Investment': [50, 100, 75],
        'Region': ['Latin America', 'Asia', 'Global'],
        'Product_Type': ['Premium', 'Volume', 'Advanced']
    })
    
    # Gantt chart
    fig4 = go.Figure()
    
    colors = {'Latin America': '#1f77b4', 'Asia': '#ff7f0e', 'Global': '#2ca02c'}
    
    for i, row in phases_data.iterrows():
        fig4.add_trace(go.Scatter(
            x=[row['Start_Year'], row['End_Year'], row['End_Year'], row['Start_Year'], row['Start_Year']],
            y=[i, i, i+0.8, i+0.8, i],
            fill='toself',
            fillcolor=colors[row['Region']],
            line=dict(color=colors[row['Region']], width=2),
            name=row['Phase'],
            showlegend=True,
            hoverinfo='text',
            hovertext=f"{row['Phase']}<br>Investment: ${row['Investment']}M<br>Region: {row['Region']}"
        ))
    
    fig4.update_layout(
        title='Implementation Timeline',
        xaxis_title='Year',
        yaxis_title='Phase',
        yaxis=dict(
            tickmode='array',
            tickvals=[0.4, 1.4, 2.4],
            ticktext=phases_data['Phase'].tolist()
        ),
        height=300,
        showlegend=True
    )
    
    st.plotly_chart(fig4, use_container_width=True)
    
    # Strategic KPIs
    st.markdown('<h3 class="section-header">Strategic KPIs</h3>', unsafe_allow_html=True)
    
    # KPI projections
    kpi_data = pd.DataFrame({
        'Year': [2024, 2025, 2026, 2027, 2028],
        'Market_Penetration_LA': [0, 1, 2, 3, 5],
        'Market_Penetration_Asia': [0, 0, 1, 2, 3],
        'ROI_Percentage': [0, 5, 12, 18, 22],
        'Revenue_Millions': [0, 25, 75, 150, 250]
    })
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Market penetration
        fig5 = go.Figure()
        fig5.add_trace(go.Scatter(
            x=kpi_data['Year'],
            y=kpi_data['Market_Penetration_LA'],
            mode='lines+markers',
            name='Latin America',
            line=dict(color='#1f77b4', width=3)
        ))
        fig5.add_trace(go.Scatter(
            x=kpi_data['Year'],
            y=kpi_data['Market_Penetration_Asia'],
            mode='lines+markers',
            name='Asia',
            line=dict(color='#ff7f0e', width=3)
        ))
        fig5.update_layout(
            title='Market Penetration Projection',
            xaxis_title='Year',
            yaxis_title='Market Penetration (%)',
            height=400
        )
        st.plotly_chart(fig5, use_container_width=True)
    
    with col2:
        # ROI projection
        fig6 = go.Figure()
        fig6.add_trace(go.Scatter(
            x=kpi_data['Year'],
            y=kpi_data['ROI_Percentage'],
            mode='lines+markers',
            name='ROI',
            line=dict(color='#2ca02c', width=3),
            fill='tonexty'
        ))
        fig6.update_layout(
            title='ROI Projection',
            xaxis_title='Year',
            yaxis_title='ROI (%)',
            height=400
        )
        st.plotly_chart(fig6, use_container_width=True)
    
    # Financial investment summary
    st.markdown('<h3 class="section-header">Financial Investment Summary</h3>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Total Investment",
            value="$225M",
            delta="5-year plan"
        )
    
    with col2:
        st.metric(
            label="Expected ROI",
            value="22%",
            delta="Year 5"
        )
    
    with col3:
        st.metric(
            label="Payback Period",
            value="5-7 years",
            delta="Conservative estimate"
        )
    
    with col4:
        st.metric(
            label="Market Penetration",
            value="8%",
            delta="Combined target"
        )
    
    # Investment distribution
    col1, col2 = st.columns(2)
    
    with col1:
        fig7 = px.pie(
            phases_data,
            values='Investment',
            names='Phase',
            title='Investment Distribution by Phase',
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        fig7.update_layout(height=400)
        st.plotly_chart(fig7, use_container_width=True)
    
    with col2:
        # Revenue projection
        fig8 = go.Figure()
        fig8.add_trace(go.Scatter(
            x=kpi_data['Year'],
            y=kpi_data['Revenue_Millions'],
            mode='lines+markers',
            name='Revenue',
            line=dict(color='#d62728', width=3),
            fill='tonexty'
        ))
        fig8.update_layout(
            title='Revenue Projection',
            xaxis_title='Year',
            yaxis_title='Revenue (Millions USD)',
            height=400
        )
        st.plotly_chart(fig8, use_container_width=True)
    
    # Risk mitigation
    st.markdown('<h3 class="section-header">Risk Mitigation Strategies</h3>', unsafe_allow_html=True)
    
    risk_strategies = {
        'Geopolitical Risk': 'Diversify across multiple regions to reduce dependency on single markets',
        'Economic Risk': 'Implement currency hedging strategies and flexible pricing models',
        'Operational Risk': 'Establish multiple suppliers and distribution centers for redundancy',
        'Market Risk': 'Focus on premium positioning to differentiate from local competitors',
        'Financial Risk': 'Implement conservative budgeting with regular monitoring and adjustments'
    }
    
    for risk, strategy in risk_strategies.items():
        st.markdown(f"""
        <div class="highlight-box">
        <h4>{risk}</h4>
        <p>{strategy}</p>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
