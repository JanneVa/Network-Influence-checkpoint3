# TCF Strategic Dashboard

## Strategic Dashboard for International Expansion of Terra Cotta Foods

This interactive dashboard is based on hierarchical analysis of global data and provides strategic insights for the international expansion of Terra Cotta Foods (TCF) to Latin America and Asia.

### Dashboard Features

#### Executive Summary
- Key global metrics
- Fundamental strategic decisions
- Differentiated strategies by region

#### Market Analysis
- Population distribution by continent
- Total GDP and per capita analysis
- Top countries by different metrics
- Regional comparisons

#### Hierarchical Visualizations
- **Population Treemap**: Population distribution by continent and country
- **GDP Treemap**: Global economic concentration
- **Sunburst Chart**: Continental hierarchical navigation
- **Dendrogram**: Clustering of similar markets

#### Organizational Structure
- TCF structure visualization
- Employee distribution by department
- Team and resource analysis

#### Strategic Recommendations
- Complete strategic framework
- Implementation roadmap
- KPIs and tracking metrics
- Risk mitigation strategies

### Installation and Usage

#### Option 1: Automatic Execution
```bash
python run_dashboard.py
```

#### Option 2: Manual Execution
```bash
# Install dependencies
pip install -r requirements_dashboard.txt

# Run dashboard
streamlit run tcf_strategic_dashboard_english.py
```

### Required Files

- `tcf_strategic_dashboard_english.py` - Main dashboard
- `country_gdp_population.csv` - Country and GDP data
- `org_structure.csv` - Organizational structure
- `requirements_dashboard.txt` - Python dependencies

### Key Strategic Decisions

#### Latin America - Premium Products
- **Priority countries**: Brazil, Mexico, Argentina, Chile
- **Strategy**: Distribution centers for high-quality products
- **Market**: Balanced (moderate population + growing GDP per capita)

#### Asia - Basic Products Volume
- **Priority countries**: China, India, Indonesia, Vietnam
- **Strategy**: Multiple distribution centers for mass coverage
- **Market**: Massive (60%+ of world population, variable GDP per capita)

### Key Metrics

- **174 countries** analyzed with complete data
- **7.7 billion** inhabitants covered
- **$127.8 trillion** total world GDP
- **$16,580** average GDP per capita

### Technologies Used

- **Streamlit**: Interactive dashboard framework
- **Plotly**: Interactive visualizations
- **Pandas**: Data manipulation
- **Scikit-learn**: Hierarchical clustering
- **Matplotlib/Seaborn**: Static visualizations
- **Squarify**: Static treemaps

### Included Visualizations

1. **Interactive Treemap**: Quick market comparison
2. **Sunburst Chart**: Regional → country hierarchical navigation
3. **Dendrogram**: Identification of similar risk clusters
4. **Circular Treemap**: Resource optimization by region

### Strategic KPIs

#### Market Penetration
- % Latin America participation
- % Asia participation
- Year-over-year growth

#### ROI and Profitability
- ROI per distribution center
- Margin by region
- Supply chain efficiency

#### Risk Management
- Supplier diversification
- Geopolitical risk reduction
- Stability by market cluster

### Implementation Roadmap

#### Phase 1: Latin America Pilot (Years 1-2)
- Establish pilot centers in Brazil and Mexico
- Focus on TCF premium products
- Validate business model

#### Phase 2: Asia Expansion (Years 2-4)
- Enter Asian markets with basic products
- Establish centers in China and India
- Optimize supply chain

#### Phase 3: Optimization (Years 4-5)
- Optimize based on hierarchical data
- Scale operations according to identified patterns
- Diversify suppliers

### Risk Mitigation

- **Geographic diversification**: Don't depend on a single region
- **Cluster analysis**: Use dendrogram to identify similar markets
- **Resource optimization**: Apply circular treemap for center location
- **Continuous monitoring**: Track strategic KPIs

### Support

For questions or technical support, contact the TCF data analysis team.

---

**Developed for Terra Cotta Foods - Marco Antonelli, CEO**
**CheckPoint 2 - Hierarchical Data Visualization**
