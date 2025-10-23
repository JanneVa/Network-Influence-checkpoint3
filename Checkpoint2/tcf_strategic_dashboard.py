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
        background-color: #e8f5e8;
        padding: 1.5rem;
        border-radius: 0.5rem;
        border-left: 4px solid #2E8B57;
        margin: 1rem 0;
    }
    .warning-box {
        background-color: #fff3cd;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #ffc107;
        margin: 1rem 0;
    }
    .success-box {
        background-color: #d4edda;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #28a745;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    """Load and preprocess the data"""
    try:
        # Load country data
        country_data = pd.read_csv("country_gdp_population.csv")
        country_data_clean = country_data.dropna(subset=['population', 'gdp_per_capita'])
        country_data_clean['gdp_total'] = country_data_clean['population'] * country_data_clean['gdp_per_capita']
        
        # Load organization data
        org_data = pd.read_csv("org_structure.csv")
        
        return country_data_clean, org_data
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None, None

def create_treemap_population(data):
    """Create population treemap"""
    fig = px.treemap(data,
                     path=['continent', 'country'],
                     values='population',
                     color='gdp_per_capita',
                     color_continuous_scale='Blues',
                     title='Population Distribution by Continent and Country')
    fig.update_layout(height=600)
    return fig

def create_treemap_gdp(data):
    """Create GDP treemap"""
    fig = px.treemap(data,
                     path=['continent', 'country'],
                     values='gdp_total',
                     color='gdp_per_capita',
                     color_continuous_scale='Reds',
                     title='Total GDP Distribution by Continent and Country')
    fig.update_layout(height=600)
    return fig

def create_sunburst_chart(data):
    """Create sunburst chart"""
    fig = px.sunburst(data,
                      path=['continent', 'country'],
                      values='population',
                      color='gdp_per_capita',
                      color_continuous_scale='Viridis',
                      title='Continental Hierarchy of Population and GDP per Capita')
    fig.update_layout(height=700)
    return fig

def create_dendrogram(data):
    """Create hierarchical clustering dendrogram"""
    # Prepare data for clustering
    features = data[['population', 'gdp_per_capita']].values
    scaler = StandardScaler()
    features_normalized = scaler.fit_transform(features)
    
    # Calculate linkage matrix
    distances = pdist(features_normalized, metric='euclidean')
    linkage_matrix = linkage(distances, method='ward')
    
    # Create dendrogram
    fig, ax = plt.subplots(figsize=(20, 10))
    
    dendro = dendrogram(linkage_matrix,
                        labels=data['country'].values,
                        leaf_font_size=8,
                        color_threshold=2.0,
                        above_threshold_color='#888888',
                        ax=ax)
    
    ax.set_title('Hierarchical Clustering Dendrogram\nCountries grouped by Population and GDP per Capita',
                 fontsize=16, weight='bold', pad=20)
    ax.set_xlabel('Countries', fontsize=12, weight='bold')
    ax.set_ylabel('Euclidean Distance', fontsize=12, weight='bold')
    ax.tick_params(axis='x', rotation=90, labelsize=8)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    ax.axhline(y=2.0, color='red', linestyle='--', linewidth=2, alpha=0.7, label='Threshold')
    ax.legend()
    
    plt.tight_layout()
    return fig

def create_org_treemap(org_data):
    """Create organizational structure treemap"""
    fig = px.treemap(org_data,
                     path=['parents', 'labels'],
                     values='values',
                     title='Organizational Structure - Employee Distribution')
    fig.update_layout(height=600)
    return fig

def main():
    # Header
    st.markdown('<h1 class="main-header">TCF Strategic Dashboard</h1>', unsafe_allow_html=True)
    st.markdown('<h2 style="text-align: center; color: #666;">Strategic Analysis for International Expansion of Terra Cotta Foods</h2>', unsafe_allow_html=True)
    
    # Load data
    country_data, org_data = load_data()
    
    if country_data is None or org_data is None:
        st.error("Could not load data. Please verify that CSV files are available.")
        return
    
    # Sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox(
        "Select a section:",
        ["Executive Summary", "Market Analysis", "Hierarchical Visualizations", 
         "Organizational Structure", "Strategic Recommendations"]
    )
    
    # Key metrics in sidebar
    st.sidebar.markdown("### Key Metrics")
    total_countries = len(country_data)
    total_population = country_data['population'].sum()
    avg_gdp_per_capita = country_data['gdp_per_capita'].mean()
    
    st.sidebar.metric("Countries Analyzed", f"{total_countries:,}")
    st.sidebar.metric("Total Population", f"{total_population:,.0f}")
    st.sidebar.metric("Average GDP per Capita", f"${avg_gdp_per_capita:,.0f}")
    
    # Main content based on selected page
    if page == "Executive Summary":
        show_executive_summary(country_data)
    elif page == "Market Analysis":
        show_market_analysis(country_data)
    elif page == "Hierarchical Visualizations":
        show_hierarchical_visualizations(country_data)
    elif page == "Organizational Structure":
        show_organizational_analysis(org_data)
    elif page == "Strategic Recommendations":
        show_strategic_recommendations(country_data)

def show_executive_summary(country_data):
    """Show executive summary page"""
    st.markdown('<h2 class="section-header">Executive Summary</h2>', unsafe_allow_html=True)
    
    # Key insights
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h4>Global Coverage</h4>
            <p><strong>174 countries</strong> with complete data analyzed</p>
            <p>Coverage of <strong>7.7 billion</strong> inhabitants</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h4>Economic Potential</h4>
            <p>Total world GDP: <strong>$127.8 trillion</strong></p>
            <p>Average GDP per capita: <strong>$16,580</strong></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h4>Priority Markets</h4>
            <p><strong>Latin America:</strong> Premium products</p>
            <p><strong>Asia:</strong> Basic products volume</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Strategic decisions
    st.markdown('<h3 class="section-header">Key Strategic Decisions</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="strategy-box">
            <h4>Latin America</h4>
            <ul>
                <li><strong>Strategy:</strong> TCF premium products</li>
                <li><strong>Priority countries:</strong> Brazil, Mexico, Argentina, Chile</li>
                <li><strong>Focus:</strong> High-quality distribution centers</li>
                <li><strong>Market:</strong> Balanced (population + growing GDP)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="strategy-box">
            <h4>Asia</h4>
            <ul>
                <li><strong>Strategy:</strong> TCF basic products for volume</li>
                <li><strong>Priority countries:</strong> China, India, Indonesia, Vietnam</li>
                <li><strong>Focus:</strong> Multiple mass distribution centers</li>
                <li><strong>Market:</strong> Massive (60%+ of world population)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

def show_market_analysis(country_data):
    """Show market analysis page"""
    st.markdown('<h2 class="section-header">Market Analysis</h2>', unsafe_allow_html=True)
    
    # Continent analysis
    continent_analysis = country_data.groupby('continent').agg({
        'population': ['sum', 'count'],
        'gdp_per_capita': 'mean',
        'gdp_total': 'sum'
    }).round(2)
    
    continent_analysis.columns = ['Total_Population', 'Num_Countries', 'Avg_GDP_per_capita', 'Total_GDP']
    continent_analysis = continent_analysis.sort_values('Total_Population', ascending=False)
    
    st.markdown("### Analysis by Continent")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Population distribution
        fig_pop = px.bar(continent_analysis.reset_index(),
                        x='continent', y='Total_Population',
                        title='Population Distribution by Continent',
                        color='Total_Population',
                        color_continuous_scale='Blues')
        fig_pop.update_layout(height=400)
        st.plotly_chart(fig_pop, use_container_width=True)
    
    with col2:
        # GDP distribution
        fig_gdp = px.bar(continent_analysis.reset_index(),
                        x='continent', y='Total_GDP',
                        title='Total GDP Distribution by Continent',
                        color='Total_GDP',
                        color_continuous_scale='Reds')
        fig_gdp.update_layout(height=400)
        st.plotly_chart(fig_gdp, use_container_width=True)
    
    # Top countries analysis
    st.markdown("### Top Countries by Market")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("#### By Population")
        top_population = country_data.nlargest(10, 'population')[['country', 'continent', 'population']]
        st.dataframe(top_population, use_container_width=True)
    
    with col2:
        st.markdown("#### By Total GDP")
        top_gdp = country_data.nlargest(10, 'gdp_total')[['country', 'continent', 'gdp_total']]
        st.dataframe(top_gdp, use_container_width=True)
    
    with col3:
        st.markdown("#### By GDP per Capita")
        top_gdp_per_capita = country_data.nlargest(10, 'gdp_per_capita')[['country', 'continent', 'gdp_per_capita']]
        st.dataframe(top_gdp_per_capita, use_container_width=True)

def show_hierarchical_visualizations(country_data):
    """Show hierarchical visualizations page"""
    st.markdown('<h2 class="section-header">Hierarchical Visualizations</h2>', unsafe_allow_html=True)
    
    # Visualization selector
    viz_type = st.selectbox(
        "Select visualization type:",
        ["Population Treemap", "GDP Treemap", "Sunburst Chart", "Dendrogram"]
    )
    
    if viz_type == "Population Treemap":
        st.markdown("### Population Distribution Treemap")
        fig = create_treemap_population(country_data)
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        <div class="success-box">
            <h4>Population Treemap Interpretation</h4>
            <p>• <strong>Asia dominates:</strong> 59.2% of world population</p>
            <p>• <strong>Africa:</strong> 17.7% of world population</p>
            <p>• <strong>Americas:</strong> 13.0% of world population</p>
            <p>• <strong>Europe:</strong> 9.6% of world population</p>
        </div>
        """, unsafe_allow_html=True)
    
    elif viz_type == "GDP Treemap":
        st.markdown("### GDP Distribution Treemap")
        fig = create_treemap_gdp(country_data)
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        <div class="success-box">
            <h4>GDP Treemap Interpretation</h4>
            <p>• <strong>Economic concentration:</strong> Developed countries dominate total GDP</p>
            <p>• <strong>Opportunity:</strong> Emerging markets with high potential</p>
            <p>• <strong>Strategy:</strong> Balance between volume (population) and value (GDP)</p>
        </div>
        """, unsafe_allow_html=True)
    
    elif viz_type == "Sunburst Chart":
        st.markdown("### Sunburst Chart - Continental Hierarchy")
        fig = create_sunburst_chart(country_data)
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        <div class="success-box">
            <h4>Sunburst Chart Interpretation</h4>
            <p>• <strong>Hierarchical navigation:</strong> Center → Continent → Country</p>
            <p>• <strong>Size:</strong> Proportional to population</p>
            <p>• <strong>Color:</strong> Indicates GDP per capita (darker = higher GDP)</p>
            <p>• <strong>Use:</strong> Quick identification of prosperous markets</p>
        </div>
        """, unsafe_allow_html=True)
    
    elif viz_type == "Dendrogram":
        st.markdown("### Hierarchical Clustering Dendrogram")
        fig = create_dendrogram(country_data)
        st.pyplot(fig)
        
        st.markdown("""
        <div class="success-box">
            <h4>Dendrogram Interpretation</h4>
            <p>• <strong>Similar clusters:</strong> Countries with similar economic characteristics</p>
            <p>• <strong>Risk strategy:</strong> Diversify across different clusters</p>
            <p>• <strong>Optimization:</strong> Distribution centers for similar clusters</p>
            <p>• <strong>Red threshold:</strong> Separation line between groups</p>
        </div>
        """, unsafe_allow_html=True)

def show_organizational_analysis(org_data):
    """Show organizational analysis page"""
    st.markdown('<h2 class="section-header">Organizational Structure</h2>', unsafe_allow_html=True)
    
    # Organizational treemap
    st.markdown("### Employee Distribution by Department")
    fig = create_org_treemap(org_data)
    st.plotly_chart(fig, use_container_width=True)
    
    # Department analysis
    st.markdown("### Analysis by Department")
    
    # Calculate department totals
    dept_totals = org_data.groupby('parents')['values'].sum().reset_index()
    dept_totals = dept_totals[dept_totals['parents'] != '']
    dept_totals = dept_totals.sort_values('values', ascending=False)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Bar chart of department sizes
        fig_dept = px.bar(dept_totals,
                         x='parents', y='values',
                         title='Employees by Department',
                         color='values',
                         color_continuous_scale='Greens')
        fig_dept.update_layout(height=400)
        st.plotly_chart(fig_dept, use_container_width=True)
    
    with col2:
        # Pie chart of department distribution
        fig_pie = px.pie(dept_totals,
                        values='values', names='parents',
                        title='Percentage Distribution by Department')
        fig_pie.update_layout(height=400)
        st.plotly_chart(fig_pie, use_container_width=True)
    
    # Team details
    st.markdown("### Team Details")
    team_details = org_data[org_data['parents'] != ''].sort_values('values', ascending=False)
    st.dataframe(team_details, use_container_width=True)

def show_strategic_recommendations(country_data):
    """Show strategic recommendations page"""
    st.markdown('<h2 class="section-header">Strategic Recommendations</h2>', unsafe_allow_html=True)
    
    # Strategic framework
    st.markdown("### Strategic Framework for TCF")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="strategy-box">
            <h4>LATIN AMERICA STRATEGY</h4>
            <h5>Balanced Market - Premium Products</h5>
            <ul>
                <li><strong>Brazil:</strong> 211M inhabitants, $10,280 GDP/capita</li>
                <li><strong>Mexico:</strong> 130M inhabitants, $14,158 GDP/capita</li>
                <li><strong>Argentina:</strong> 45M inhabitants, $13,858 GDP/capita</li>
                <li><strong>Chile:</strong> 19M inhabitants, $16,710 GDP/capita</li>
            </ul>
            <p><strong>Strategy:</strong> Distribution centers for high-quality products</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="strategy-box">
            <h4>ASIA STRATEGY</h4>
            <h5>Massive Market - Basic Products</h5>
            <ul>
                <li><strong>China:</strong> 1.4B inhabitants, $13,303 GDP/capita</li>
                <li><strong>India:</strong> 1.45B inhabitants, $2,697 GDP/capita</li>
                <li><strong>Indonesia:</strong> 283M inhabitants, $4,925 GDP/capita</li>
                <li><strong>Vietnam:</strong> 100M inhabitants, $4,717 GDP/capita</li>
            </ul>
            <p><strong>Strategy:</strong> Multiple centers for mass coverage</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Detailed country analysis with charts
    st.markdown("### Priority Countries Analysis")
    
    # Get specific country data
    priority_countries = ['Brazil', 'Mexico', 'Argentina', 'Chile', 'China', 'India', 'Indonesia', 'Vietnam']
    country_details = country_data[country_data['country'].isin(priority_countries)].copy()
    country_details = country_details.sort_values('gdp_total', ascending=False)
    
    # Add market type column
    country_details['Market_Type'] = country_details['country'].apply(
        lambda x: 'Premium' if x in ['Brazil', 'Mexico', 'Argentina', 'Chile'] else 'Volume'
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Population comparison chart
        fig_pop = px.bar(
            country_details,
            x='country',
            y='population',
            color='Market_Type',
            title='Population by Priority Country',
            color_discrete_map={'Premium': '#2E8B57', 'Volume': '#1f77b4'}
        )
        fig_pop.update_layout(height=400, xaxis_tickangle=-45)
        st.plotly_chart(fig_pop, use_container_width=True)
    
    with col2:
        # GDP per capita comparison
        fig_gdp = px.bar(
            country_details,
            x='country',
            y='gdp_per_capita',
            color='Market_Type',
            title='GDP per Capita by Priority Country',
            color_discrete_map={'Premium': '#2E8B57', 'Volume': '#1f77b4'}
        )
        fig_gdp.update_layout(height=400, xaxis_tickangle=-45)
        st.plotly_chart(fig_gdp, use_container_width=True)
    
    # Scatter plot: Population vs GDP per capita
    st.markdown("### Market Opportunity Analysis")
    
    fig_scatter = px.scatter(
        country_details,
        x='population',
        y='gdp_per_capita',
        size='gdp_total',
        color='Market_Type',
        hover_name='country',
        title='Market Opportunity: Population vs GDP per Capita',
        color_discrete_map={'Premium': '#2E8B57', 'Volume': '#1f77b4'},
        size_max=50
    )
    fig_scatter.update_layout(height=500)
    st.plotly_chart(fig_scatter, use_container_width=True)
    
    # Market type comparison
    col1, col2 = st.columns(2)
    
    with col1:
        # Premium markets summary
        premium_markets = country_details[country_details['Market_Type'] == 'Premium']
        st.markdown("#### Premium Markets (Latin America)")
        st.dataframe(
            premium_markets[['country', 'population', 'gdp_per_capita', 'gdp_total']].round(0),
            use_container_width=True
        )
    
    with col2:
        # Volume markets summary
        volume_markets = country_details[country_details['Market_Type'] == 'Volume']
        st.markdown("#### Volume Markets (Asia)")
        st.dataframe(
            volume_markets[['country', 'population', 'gdp_per_capita', 'gdp_total']].round(0),
            use_container_width=True
        )
    
    # Implementation roadmap with Gantt chart
    st.markdown("### Implementation Roadmap")
    
    # Gantt chart data
    gantt_data = {
        'Task': [
            'Brazil Distribution Center', 'Mexico Distribution Center', 'Premium Product Launch',
            'China Distribution Center', 'India Distribution Center', 'Indonesia Distribution Center',
            'Volume Product Launch', 'Supply Chain Optimization', 'Advanced Analytics'
        ],
        'Start': ['2024-01-01', '2024-06-01', '2024-12-01', '2025-01-01', '2025-06-01', '2026-01-01', '2026-06-01', '2027-01-01', '2027-06-01'],
        'Finish': ['2024-12-31', '2025-05-31', '2025-11-30', '2025-12-31', '2026-05-31', '2026-12-31', '2027-05-31', '2027-12-31', '2028-05-31'],
        'Phase': ['Phase 1', 'Phase 1', 'Phase 1', 'Phase 2', 'Phase 2', 'Phase 2', 'Phase 2', 'Phase 3', 'Phase 3']
    }
    
    # Create Gantt chart
    fig_gantt = px.timeline(
        gantt_data,
        x_start='Start',
        x_end='Finish',
        y='Task',
        color='Phase',
        title='Implementation Timeline',
        color_discrete_map={'Phase 1': '#2E8B57', 'Phase 2': '#1f77b4', 'Phase 3': '#ff7f0e'}
    )
    fig_gantt.update_layout(height=500)
    st.plotly_chart(fig_gantt, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="strategy-box">
            <h4>PHASE 1: Latin America (Years 1-2)</h4>
            <h5>Objectives:</h5>
            <ul>
                <li>Establish presence in premium markets</li>
                <li>Develop high-quality supply chain</li>
                <li>Build relationships with local distributors</li>
            </ul>
            <h5>Actions:</h5>
            <ul>
                <li>Distribution center in Brazil (São Paulo)</li>
                <li>Distribution center in Mexico (Mexico City)</li>
                <li>Launch of premium products</li>
            </ul>
            <h5>Estimated Investment: $50M</h5>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="strategy-box">
            <h4>PHASE 2: Asia (Years 2-4)</h4>
            <h5>Objectives:</h5>
            <ul>
                <li>Capture massive volume markets</li>
                <li>Optimize production costs</li>
                <li>Establish multiple distribution centers</li>
            </ul>
            <h5>Actions:</h5>
            <ul>
                <li>Distribution center in China (Shanghai)</li>
                <li>Distribution center in India (Mumbai)</li>
                <li>Distribution center in Indonesia (Jakarta)</li>
            </ul>
            <h5>Estimated Investment: $100M</h5>
        </div>
        """, unsafe_allow_html=True)
    
    # Phase 3
    st.markdown("""
    <div class="strategy-box">
        <h4>PHASE 3: Optimization (Years 4-5)</h4>
        <h5>Objectives:</h5>
        <ul>
            <li>Optimize based on hierarchical data analysis</li>
            <li>Scale operations according to identified patterns</li>
            <li>Diversify suppliers and reduce geopolitical risk</li>
        </ul>
        <h5>Actions:</h5>
        <ul>
            <li>Advanced analytics implementation</li>
            <li>Supply chain optimization</li>
            <li>Market expansion to secondary cities</li>
        </ul>
        <h5>Estimated Investment: $75M</h5>
    </div>
    """, unsafe_allow_html=True)
    
    # KPIs and metrics with charts
    st.markdown("### Strategic KPIs")
    
    # KPI data for projections
    kpi_data = {
        'Year': [1, 2, 3, 4, 5],
        'Market_Penetration_LA': [0, 1, 2, 3, 5],
        'Market_Penetration_Asia': [0, 0, 1, 2, 3],
        'ROI_Percentage': [0, 5, 12, 18, 22],
        'Revenue_Millions': [0, 25, 75, 150, 250]
    }
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Market penetration chart
        fig_penetration = go.Figure()
        fig_penetration.add_trace(go.Scatter(
            x=kpi_data['Year'],
            y=kpi_data['Market_Penetration_LA'],
            mode='lines+markers',
            name='Latin America',
            line=dict(color='#2E8B57', width=3)
        ))
        fig_penetration.add_trace(go.Scatter(
            x=kpi_data['Year'],
            y=kpi_data['Market_Penetration_Asia'],
            mode='lines+markers',
            name='Asia',
            line=dict(color='#1f77b4', width=3)
        ))
        fig_penetration.update_layout(
            title='Market Penetration Projection (%)',
            xaxis_title='Year',
            yaxis_title='Market Penetration (%)',
            height=400
        )
        st.plotly_chart(fig_penetration, use_container_width=True)
    
    with col2:
        # ROI projection chart
        fig_roi = px.line(
            x=kpi_data['Year'],
            y=kpi_data['ROI_Percentage'],
            title='ROI Projection (%)',
            markers=True
        )
        fig_roi.update_traces(line_color='#ff7f0e', line_width=3)
        fig_roi.update_layout(
            xaxis_title='Year',
            yaxis_title='ROI (%)',
            height=400
        )
        st.plotly_chart(fig_roi, use_container_width=True)
    
    # Revenue projection
    fig_revenue = px.area(
        x=kpi_data['Year'],
        y=kpi_data['Revenue_Millions'],
        title='Revenue Projection (Millions USD)',
        color_discrete_sequence=['#2E8B57']
    )
    fig_revenue.update_layout(
        xaxis_title='Year',
        yaxis_title='Revenue (Millions USD)',
        height=400
    )
    st.plotly_chart(fig_revenue, use_container_width=True)
    
    # KPI summary cards
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h4>Market Penetration</h4>
            <ul>
                <li>Latin America: 5% by Year 5</li>
                <li>Asia: 3% by Year 5</li>
                <li>Target: 8% combined</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h4>ROI and Profitability</h4>
            <ul>
                <li>Target ROI: 22% by Year 5</li>
                <li>Revenue: $250M by Year 5</li>
                <li>Payback: 5-7 years</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h4>Risk Management</h4>
            <ul>
                <li>Geographic diversification</li>
                <li>Supplier diversification</li>
                <li>Cluster-based optimization</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Financial summary with charts
    st.markdown("### Financial Investment Summary")
    
    # Investment data for charts
    investment_data = {
        'Phase': ['Phase 1', 'Phase 2', 'Phase 3'],
        'Investment': [50, 100, 75],
        'Region': ['Latin America', 'Asia', 'Optimization'],
        'Years': ['1-2', '2-4', '4-5'],
        'Product_Type': ['Premium', 'Volume', 'Advanced']
    }
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Investment by phase bar chart
        fig_investment = px.bar(
            x=investment_data['Phase'], 
            y=investment_data['Investment'],
            title='Investment by Phase (Millions USD)',
            color=investment_data['Investment'],
            color_continuous_scale='Blues',
            text=investment_data['Investment']
        )
        fig_investment.update_traces(texttemplate='$%{text}M', textposition='outside')
        fig_investment.update_layout(height=400)
        st.plotly_chart(fig_investment, use_container_width=True)
    
    with col2:
        # Investment pie chart
        fig_pie = px.pie(
            values=investment_data['Investment'],
            names=investment_data['Phase'],
            title='Investment Distribution by Phase',
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        fig_pie.update_traces(textposition='inside', textinfo='percent+label')
        fig_pie.update_layout(height=400)
        st.plotly_chart(fig_pie, use_container_width=True)
    
    # Timeline chart
    st.markdown("### Investment Timeline")
    
    timeline_data = {
        'Year': [1, 2, 3, 4, 5],
        'Cumulative_Investment': [25, 50, 100, 150, 225],
        'Annual_Investment': [25, 25, 50, 50, 75],
        'Phase': ['Phase 1', 'Phase 1', 'Phase 2', 'Phase 2', 'Phase 3']
    }
    
    fig_timeline = px.area(
        x=timeline_data['Year'],
        y=timeline_data['Cumulative_Investment'],
        title='Cumulative Investment Over Time',
        color_discrete_sequence=['#2E8B57']
    )
    fig_timeline.update_layout(
        height=400,
        xaxis_title='Year',
        yaxis_title='Cumulative Investment (Millions USD)'
    )
    st.plotly_chart(fig_timeline, use_container_width=True)
    
    # Total investment
    st.markdown("""
    <div class="success-box">
        <h4>Total Investment Required: $225M</h4>
        <p><strong>Expected ROI:</strong> 15-20% annually after Year 3</p>
        <p><strong>Payback Period:</strong> 5-7 years</p>
        <p><strong>Market Penetration Target:</strong> 5% in priority markets by Year 5</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Risk mitigation
    st.markdown("### Risk Mitigation")
    
    st.markdown("""
    <div class="warning-box">
        <h4>Mitigation Strategies</h4>
        <ul>
            <li><strong>Geographic diversification:</strong> Don't depend on a single region</li>
            <li><strong>Cluster analysis:</strong> Use dendrogram to identify similar markets</li>
            <li><strong>Resource optimization:</strong> Apply circular treemap for center location</li>
            <li><strong>Continuous monitoring:</strong> Track strategic KPIs</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
