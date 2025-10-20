# Streaming Visualization Portfolio (PU-2)

Tema: Visual Analytics para una plataforma de streaming (audiencias, contenido, regiones, tiempo). Objetivo: Narrativa WHO-WHAT-HOW y dashboard ejecutivo con vistas jerarquicas, relacionales, espaciales y temporales.

Datasets:
* Catalogo de titulos (genero, subgenero, duracion, rating)
* Consumo (views, watch_time, completion_rate por fecha-pais-titulo)
* Usuarios agregados (tier, dispositivo, region)
* Calendario de lanzamientos y campañas

KPI:
* MAU/DAU, conversion rate, churn, ARPU
* Watch time, completion rate, CTR de recomendacion
* Top/bottom titulos por region

Calidad y accesibilidad:
* Sin pie/donut, sin 3D, barras baseline cero
* Paletas ColorBrewer, contraste AA
* Intervalos temporales consistentes, ejes honestos

---

# Hierarchical Data Visualization Project (Checkpoint 2)

## 📊 Project Overview

This project demonstrates comprehensive hierarchical data visualization techniques using Python, focusing on global population/economic data and organizational structures. The project implements four main visualization types: Treemaps, Dendrograms, Sunburst Charts, and Circular Treemaps.

## 🎯 Objectives

- **Develop Skills**: Master hierarchical data visualization techniques
- **Apply Methods**: Implement Treemaps, Dendrograms, Sunburst Charts, and Circular Treemaps
- **Analyze Data**: Work with global country data and organizational structures
- **Compare Techniques**: Evaluate effectiveness of different visualization approaches
- **Generate Insights**: Extract actionable insights from hierarchical data

## 📁 Project Structure

```
streaming-analytics-project/
├── Checkpoint2/                          # Main project directory
│   ├── 01_hierarchical_analysis.ipynb   # Complete Jupyter notebook
│   ├── country_gdp_population.csv       # Global country dataset
│   ├── org_structure.csv                # Organizational structure dataset
│   ├── app.py                           # Streamlit dashboard
│   ├── custom.css                       # Dashboard styling
│   ├── requirements.txt                 # Python dependencies
│   ├── clean_hierarchical_data.py       # Data cleaning script
│   ├── prepare_hierarchical_data.py     # Data preparation script
│   ├── generate_hierarchical.py         # Visualization generation script
│   ├── generate_hierarchical_viz.py     # Advanced visualization script
│   ├── phase1-hierarchical-storyboard.pdf # Visual planning document
│   ├── who-what-how-framework.md        # Audience and strategy framework
│   ├── big-ideas.md                     # Core insights and messages
│   └── design-rationale.md              # Visualization design justification
├── data/                                # Data directory
├── etl/                                 # ETL pipelines
├── notebooks/                           # Additional notebooks
├── sql/                                 # SQL queries and scripts
└── README.md                            # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Git (for cloning the repository)

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd streaming-analytics-project
   ```

2. **Navigate to Checkpoint2:**
   ```bash
   cd Checkpoint2
   ```

3. **Create virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Project

#### Option 1: Jupyter Notebook (Recommended for Analysis)
```bash
jupyter notebook 01_hierarchical_analysis.ipynb
```

#### Option 2: Interactive Dashboard
```bash
streamlit run app.py
```

#### Option 3: Generate Visualizations
```bash
# Clean and prepare data
python clean_hierarchical_data.py
python prepare_hierarchical_data.py

# Generate visualizations
python generate_hierarchical.py
python generate_hierarchical_viz.py
```

## 📊 Datasets

### Global Country Data (`country_gdp_population.csv`)
- **Source**: World Bank API + Rest Countries API
- **Records**: 193 UN Member Countries
- **Columns**: 
  - `Continent`: Geographic region
  - `Country`: Country name
  - `Population`: Total population
  - `Gdp_per_capita`: GDP per capita in USD

### Organizational Structure (`org_structure.csv`)
- **Source**: Synthetic tech company data
- **Records**: 33 organizational units
- **Columns**:
  - `labels`: Unit name
  - `parents`: Parent unit
  - `values`: Number of employees

## 🎨 Visualization Techniques

### 1. Treemap (Static & Interactive)
- **Purpose**: Show proportional relationships in hierarchical data
- **Implementation**: 
  - Static: `squarify` library
  - Interactive: `plotly.express.treemap`
- **Use Case**: Population distribution, resource allocation

### 2. Dendrogram (Hierarchical Clustering)
- **Purpose**: Reveal clustering patterns and similarities
- **Implementation**: `scipy.cluster.hierarchy`
- **Use Case**: Country similarity analysis, pattern discovery

### 3. Sunburst Chart
- **Purpose**: Navigate hierarchical structures intuitively
- **Implementation**: `plotly.graph_objects.Sunburst`
- **Use Case**: Geographic hierarchy, organizational structure

### 4. Circular Treemap (Icicle)
- **Purpose**: Show resource flow and allocation
- **Implementation**: `plotly.express.icicle`
- **Use Case**: Budget distribution, economic analysis

## 🛠️ Technical Stack

### Core Libraries
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **matplotlib**: Static plotting
- **seaborn**: Statistical visualization
- **plotly**: Interactive visualizations
- **squarify**: Treemap generation
- **scipy**: Scientific computing and clustering
- **scikit-learn**: Machine learning utilities

### Dashboard Framework
- **streamlit**: Interactive web application
- **HTML/CSS**: Custom styling and layout

### Development Tools
- **jupyter**: Interactive development environment
- **ipykernel**: Jupyter kernel management

## 📈 Key Insights

### Global Patterns
- **Population Concentration**: Asia dominates with 60%+ of global population
- **Economic Distribution**: GDP concentrated in specific regions
- **Development Clustering**: Countries group by development patterns, not geography
- **Correlation**: Negative correlation between population size and GDP per capita

### Organizational Insights
- **Resource Allocation**: Engineering and Sales receive highest budget allocation
- **Efficiency Patterns**: Employee-to-budget ratios vary significantly by department
- **Hierarchical Structure**: Clear organizational hierarchy enables efficient management

### Visualization Effectiveness
- **Treemaps**: Best for proportional comparisons and executive presentations
- **Dendrograms**: Ideal for pattern discovery and clustering analysis
- **Sunburst Charts**: Excellent for hierarchical navigation and multi-level display
- **Circular Treemaps**: Perfect for resource allocation and flow visualization

## 🎯 Use Cases

### For Data Analysts
- Learn hierarchical visualization techniques
- Understand when to use different visualization methods
- Practice with real-world datasets
- Develop interactive dashboard skills

### For Business Intelligence
- Analyze organizational resource allocation
- Understand global economic patterns
- Create executive-level visualizations
- Make data-driven strategic decisions

### For Data Science Students
- Study visualization best practices
- Practice with comprehensive datasets
- Learn interactive visualization techniques
- Understand hierarchical data structures

## 📚 Documentation

### Project Documentation
- **`phase1-hierarchical-storyboard.pdf`**: Visual planning and narrative flow
- **`who-what-how-framework.md`**: Audience analysis and data strategy
- **`big-ideas.md`**: Core insights and key messages
- **`design-rationale.md`**: Justification for visualization choices

### Code Documentation
- **Inline Comments**: Detailed code explanations
- **Docstrings**: Function and class documentation
- **Logging**: Comprehensive logging for debugging
- **Error Handling**: Robust error handling throughout

## 🔧 Scripts and Automation

### Data Processing Scripts
- **`clean_hierarchical_data.py`**: Data validation and cleaning
- **`prepare_hierarchical_data.py`**: Data preparation and feature engineering

### Visualization Generation Scripts
- **`generate_hierarchical.py`**: Standard visualization generation
- **`generate_hierarchical_viz.py`**: Advanced visualization features

### Usage Examples
```bash
# Clean data with verbose output
python clean_hierarchical_data.py --verbose

# Prepare data for specific output directory
python prepare_hierarchical_data.py --output-dir ./prepared_data

# Generate visualizations with custom settings
python generate_hierarchical.py --input-dir ./prepared_data --output-dir ./visualizations
```

## 🎨 Customization

### Color Schemes
- **Geographic Data**: Blues (water/ocean association)
- **Economic Data**: Reds (attention-grabbing, important metrics)
- **Organizational Data**: Greens (growth, financial context)
- **Clustering Data**: Multi-color (distinction, accessibility)

### Layout Options
- **Static Figures**: 12x8 for detailed analysis
- **Interactive Charts**: 900x900 for optimal viewing
- **Dashboard Elements**: 1000x600 for comprehensive overview

### Interactive Features
- **Hover Information**: Detailed metrics on demand
- **Zoom Capabilities**: Drill-down functionality
- **Filter Options**: Dynamic data filtering
- **Export Features**: Save visualizations in multiple formats

## 🚀 Advanced Features

### Dashboard Features
- **Multi-tab Interface**: Organized visualization sections
- **Interactive Filters**: Dynamic data exploration
- **Real-time Metrics**: Live data summaries
- **Responsive Design**: Works on different screen sizes

### Visualization Enhancements
- **Multiple Clustering Methods**: Ward, complete, average, single
- **Advanced Color Palettes**: Custom color schemes
- **Statistical Analysis**: Correlation matrices, distribution analysis
- **Export Options**: PNG, HTML, PDF formats

## 🔍 Troubleshooting

### Common Issues

#### Import Errors
```bash
# Ensure virtual environment is activated
source venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

#### Data Loading Issues
```bash
# Check file paths
ls -la *.csv

# Verify data format
python -c "import pandas as pd; print(pd.read_csv('country_gdp_population.csv').head())"
```

#### Visualization Rendering Issues
```bash
# Update plotly
pip install plotly --upgrade

# Clear matplotlib cache
rm -rf ~/.matplotlib
```

### Performance Optimization
- **Large Datasets**: Use data sampling for initial exploration
- **Memory Issues**: Process data in chunks
- **Rendering Speed**: Reduce figure complexity for large datasets

## 🤝 Contributing

### Development Setup
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

### Code Style
- Follow PEP 8 guidelines
- Use meaningful variable names
- Add docstrings to functions
- Include error handling

### Testing
```bash
# Run data validation
python clean_hierarchical_data.py --verbose

# Test visualization generation
python generate_hierarchical.py --verbose
```

## 📄 License

This project is part of an educational curriculum and is intended for learning purposes. Please respect the academic integrity guidelines when using this code.

## 🙏 Acknowledgments

- **World Bank**: For providing global economic data
- **Rest Countries API**: For geographic information
- **Python Community**: For excellent visualization libraries
- **Streamlit**: For the interactive dashboard framework

## 📞 Support

For questions or issues:
1. Check the troubleshooting section
2. Review the documentation files
3. Examine the code comments
4. Create an issue in the repository

## 🔄 Updates and Maintenance

### Regular Updates
- **Data Refresh**: Update country data quarterly
- **Dependency Updates**: Keep libraries current
- **Documentation**: Maintain up-to-date documentation
- **Performance**: Monitor and optimize performance

### Version History
- **v1.0**: Initial implementation with basic visualizations
- **v1.1**: Added interactive dashboard
- **v1.2**: Enhanced with advanced features
- **v1.3**: Comprehensive documentation and automation

---

**Happy Visualizing! 📊✨**

*This project demonstrates the power of hierarchical data visualization in understanding complex relationships and patterns in both global and organizational contexts.*