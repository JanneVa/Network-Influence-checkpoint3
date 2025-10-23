# TCF Strategic Dashboard

## 📊 Overview

This repository contains a comprehensive Streamlit dashboard for Terra Cotta Foods (TCF) strategic expansion analysis. The dashboard provides interactive visualizations and strategic recommendations for TCF's expansion into Latin America and Asia markets.

## 🎯 Key Features

- **Interactive Hierarchical Analysis**: Treemaps, sunburst charts, and dendrograms
- **Strategic Recommendations**: Data-driven insights for market expansion
- **Financial Projections**: ROI analysis and investment planning
- **Risk Assessment**: Comprehensive risk analysis with mitigation strategies
- **Market Analysis**: Country prioritization and opportunity scoring
- **Implementation Timeline**: Detailed project roadmap

## 📁 Repository Structure

```
├── tcf_strategic_dashboard.py          # Main Streamlit dashboard
├── run_dashboard.py                    # Dashboard runner script
├── requirements_dashboard.txt          # Python dependencies
├── country_gdp_population.csv          # Country market data
├── org_structure.csv                   # Organizational structure data
├── 01_hierarchical_analysis.ipynb      # Original analysis notebook
├── TCF_Strategic_Dashboard_Tables.xlsx # Excel tables for Looker/BI tools
├── generate_excel_tables.py            # Script to generate Excel tables
├── README.md                           # This file
└── .gitignore                          # Git ignore file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Checkpoint2
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv dashboard_env
   source dashboard_env/bin/activate  # On Windows: dashboard_env\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements_dashboard.txt
   ```

4. **Run the dashboard**
   ```bash
   python run_dashboard.py
   ```
   
   Or manually:
   ```bash
   streamlit run tcf_strategic_dashboard.py --server.port 8501
   ```

5. **Access the dashboard**
   - Open your browser and go to: `http://localhost:8501`

## 📊 Dashboard Sections

### 1. **Executive Summary**
- Key strategic decisions
- Investment overview
- Market opportunity highlights

### 2. **Hierarchical Analysis**
- Interactive treemaps
- Sunburst charts
- Dendrograms for market clustering

### 3. **Strategic Recommendations**
- **Priority Countries Analysis**: Population and GDP analysis
- **Implementation Roadmap**: Gantt chart with project timeline
- **Strategic KPIs**: Market penetration and ROI projections
- **Financial Investment Summary**: Investment distribution and returns
- **Risk Mitigation**: Risk assessment and strategies

## 📈 Key Strategic Insights

### **Expansion Strategy**
- **Latin America**: Premium products focus (Brazil, Mexico, Argentina, Chile)
- **Asia**: Volume products focus (China, India, Indonesia, Vietnam)

### **Financial Projections**
- **Total Investment**: $225M over 5 years
- **Expected ROI**: 22% by year 5
- **Revenue Target**: $250M by year 5
- **Market Penetration**: 8% combined by year 5

### **Implementation Phases**
1. **Phase 1 (2024-2025)**: Latin America expansion - $50M
2. **Phase 2 (2025-2027)**: Asia expansion - $100M
3. **Phase 3 (2027-2028)**: Optimization - $75M

## 📊 Data Sources

### **CSV Files**
- `country_gdp_population.csv`: Country-level market data
- `org_structure.csv`: TCF organizational structure

### **Excel Tables** (for BI tools)
- `TCF_Strategic_Dashboard_Tables.xlsx`: 9 comprehensive tables
  - Implementation Phases
  - Priority Countries
  - Implementation Tasks
  - Financial Metrics
  - KPI Projections
  - Risk Analysis
  - Organizational Structure
  - Market Analysis
  - Summary

## 🔧 Technical Details

### **Dependencies**
- `streamlit`: Web application framework
- `plotly`: Interactive visualizations
- `pandas`: Data manipulation
- `numpy`: Numerical computing
- `scipy`: Scientific computing
- `scikit-learn`: Machine learning
- `openpyxl`: Excel file handling

### **Browser Compatibility**
- Chrome (recommended)
- Firefox
- Safari
- Edge

## 📋 Usage Instructions

### **Running the Dashboard**
1. Ensure all dependencies are installed
2. Run `python run_dashboard.py` or `streamlit run tcf_strategic_dashboard.py`
3. Open browser to the provided URL
4. Navigate through different sections using the sidebar

### **Using Excel Tables**
1. Open `TCF_Strategic_Dashboard_Tables.xlsx`
2. Import relevant sheets into your BI tool (Looker, Power BI, Tableau)
3. Create visualizations based on the provided data structure
4. Reference `EXCEL_TABLES_GUIDE.md` for detailed instructions

## 🎯 Target Audience

- **Executives**: Strategic decision making
- **Business Analysts**: Market analysis and insights
- **Project Managers**: Implementation planning
- **Financial Teams**: Investment and ROI analysis
- **Risk Managers**: Risk assessment and mitigation

## 📚 Additional Resources

- `01_hierarchical_analysis.ipynb`: Original analysis methodology
- `EXCEL_TABLES_GUIDE.md`: Detailed guide for using Excel tables
- `README_DASHBOARD_ENGLISH.md`: Additional dashboard documentation

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is part of the Visual Modeling for Information course.

## 🆘 Support

For questions or issues:
1. Check the documentation files
2. Review the original analysis notebook
3. Contact the development team

## 🔄 Updates

- **v1.0**: Initial dashboard with hierarchical analysis
- **v1.1**: Added strategic recommendations with visualizations
- **v1.2**: Excel tables for BI tools integration
- **v1.3**: Complete documentation and setup guide

---

**Ready to explore TCF's strategic expansion opportunities!** 🚀
