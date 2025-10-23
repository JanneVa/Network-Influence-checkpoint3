import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def create_implementation_phases():
    """Create implementation phases data"""
    data = {
        'phase_id': [1, 2, 3],
        'phase_name': ['Phase 1', 'Phase 2', 'Phase 3'],
        'start_year': [2024, 2025, 2027],
        'end_year': [2025, 2027, 2028],
        'investment_amount': [50000000, 100000000, 75000000],
        'region': ['Latin America', 'Asia', 'Optimization'],
        'product_type': ['Premium', 'Volume', 'Advanced'],
        'objective_1': [
            'Establish presence in premium markets',
            'Capture massive volume markets',
            'Optimize based on hierarchical data analysis'
        ],
        'objective_2': [
            'Develop high-quality supply chain',
            'Optimize production costs',
            'Scale operations according to identified patterns'
        ],
        'objective_3': [
            'Build relationships with local distributors',
            'Establish multiple distribution centers',
            'Diversify suppliers and reduce geopolitical risk'
        ],
        'action_1': [
            'Distribution center in Brazil (São Paulo)',
            'Distribution center in China (Shanghai)',
            'Advanced analytics implementation'
        ],
        'action_2': [
            'Distribution center in Mexico (Mexico City)',
            'Distribution center in India (Mumbai)',
            'Supply chain optimization'
        ],
        'action_3': [
            'Launch of premium products',
            'Distribution center in Indonesia (Jakarta)',
            'Market expansion to secondary cities'
        ]
    }
    return pd.DataFrame(data)

def create_priority_countries():
    """Create priority countries data"""
    data = {
        'country_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        'country_name': ['Brazil', 'Mexico', 'Argentina', 'Chile', 'China', 'India', 'Indonesia', 'Vietnam', 'Colombia', 'Peru', 'Thailand', 'Malaysia'],
        'continent': ['Americas', 'Americas', 'Americas', 'Americas', 'Asia', 'Asia', 'Asia', 'Asia', 'Americas', 'Americas', 'Asia', 'Asia'],
        'population': [211998573, 130861007, 45696159, 19764771, 1408975000, 1450935791, 283487931, 100987686, 52886363, 34217848, 71668011, 35557673],
        'gdp_per_capita': [10280.31, 14157.94, 13858.20, 16709.89, 13303.15, 2696.66, 4925.43, 4717.29, 7913.99, 8452.37, 7345.14, 11867.26],
        'gdp_total': [2179000000000, 1853000000000, 633000000000, 330000000000, 18740000000000, 3910000000000, 1395000000000, 476000000000, 418000000000, 289000000000, 526000000000, 422000000000],
        'market_type': ['Premium', 'Premium', 'Premium', 'Premium', 'Volume', 'Volume', 'Volume', 'Volume', 'Premium', 'Premium', 'Volume', 'Volume'],
        'priority_level': [1, 1, 2, 2, 1, 1, 2, 2, 3, 3, 3, 3],
        'region': ['Latin America', 'Latin America', 'Latin America', 'Latin America', 'Asia', 'Asia', 'Asia', 'Asia', 'Latin America', 'Latin America', 'Asia', 'Asia'],
        'market_opportunity_score': [85, 82, 75, 78, 95, 88, 72, 68, 65, 62, 70, 73],
        'population_millions': [212, 131, 46, 20, 1409, 1451, 283, 101, 53, 34, 72, 36],
        'gdp_billions': [2179, 1853, 633, 330, 18740, 3910, 1395, 476, 418, 289, 526, 422]
    }
    return pd.DataFrame(data)

def create_implementation_tasks():
    """Create implementation tasks data"""
    data = {
        'task_id': [1, 2, 3, 4, 5, 6, 7, 8, 9],
        'task_name': [
            'Brazil Distribution Center',
            'Mexico Distribution Center', 
            'Premium Product Launch',
            'China Distribution Center',
            'India Distribution Center',
            'Indonesia Distribution Center',
            'Volume Product Launch',
            'Supply Chain Optimization',
            'Advanced Analytics'
        ],
        'start_date': [
            '2024-01-01', '2024-06-01', '2024-12-01',
            '2025-01-01', '2025-06-01', '2026-01-01',
            '2026-06-01', '2027-01-01', '2027-06-01'
        ],
        'end_date': [
            '2024-12-31', '2025-05-31', '2025-11-30',
            '2025-12-31', '2026-05-31', '2026-12-31',
            '2027-05-31', '2027-12-31', '2028-05-31'
        ],
        'phase': ['Phase 1', 'Phase 1', 'Phase 1', 'Phase 2', 'Phase 2', 'Phase 2', 'Phase 2', 'Phase 3', 'Phase 3'],
        'country': ['Brazil', 'Mexico', 'Latin America', 'China', 'India', 'Indonesia', 'Asia', 'Global', 'Global'],
        'status': ['Planned', 'Planned', 'Planned', 'Planned', 'Planned', 'Planned', 'Planned', 'Planned', 'Planned'],
        'investment_amount': [25000000, 25000000, 0, 40000000, 35000000, 25000000, 0, 40000000, 35000000],
        'task_type': ['Infrastructure', 'Infrastructure', 'Product', 'Infrastructure', 'Infrastructure', 'Infrastructure', 'Product', 'Operations', 'Technology'],
        'priority': ['High', 'High', 'High', 'High', 'High', 'Medium', 'High', 'Medium', 'Medium'],
        'duration_days': [365, 365, 365, 365, 365, 365, 365, 365, 365]
    }
    return pd.DataFrame(data)

def create_financial_metrics():
    """Create financial metrics data"""
    data = {
        'metric_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        'metric_name': [
            'Total Investment', 'Phase 1 Investment', 'Phase 2 Investment', 'Phase 3 Investment',
            'Expected ROI', 'Payback Period', 'Market Penetration Target', 'Revenue Target',
            'Brazil Investment', 'Mexico Investment', 'China Investment', 'India Investment',
            'Indonesia Investment', 'LA Market Penetration', 'Asia Market Penetration'
        ],
        'metric_category': [
            'Investment', 'Investment', 'Investment', 'Investment',
            'Performance', 'Performance', 'Performance', 'Performance',
            'Investment', 'Investment', 'Investment', 'Investment',
            'Investment', 'Performance', 'Performance'
        ],
        'phase': [
            'All Phases', 'Phase 1', 'Phase 2', 'Phase 3',
            'All Phases', 'All Phases', 'All Phases', 'All Phases',
            'Phase 1', 'Phase 1', 'Phase 2', 'Phase 2',
            'Phase 2', 'Phase 1', 'Phase 2'
        ],
        'value': [
            225000000, 50000000, 100000000, 75000000,
            22, 6, 8, 250000000,
            25000000, 25000000, 40000000, 35000000,
            25000000, 5, 3
        ],
        'unit': [
            'USD', 'USD', 'USD', 'USD',
            'Percent', 'Years', 'Percent', 'USD',
            'USD', 'USD', 'USD', 'USD',
            'USD', 'Percent', 'Percent'
        ],
        'description': [
            'Total investment required for all phases',
            'Investment for Latin America expansion',
            'Investment for Asia expansion',
            'Investment for optimization phase',
            'Expected ROI by year 5',
            'Expected payback period',
            'Target market penetration by year 5',
            'Target revenue by year 5',
            'Investment in Brazil distribution center',
            'Investment in Mexico distribution center',
            'Investment in China distribution center',
            'Investment in India distribution center',
            'Investment in Indonesia distribution center',
            'Latin America market penetration target',
            'Asia market penetration target'
        ],
        'target_year': [2028, 2025, 2027, 2028, 2028, 2028, 2028, 2028, 2024, 2024, 2025, 2025, 2026, 2028, 2028]
    }
    return pd.DataFrame(data)

def create_kpi_projections():
    """Create KPI projections data"""
    data = {
        'projection_id': [1, 2, 3, 4, 5],
        'year': [2024, 2025, 2026, 2027, 2028],
        'market_penetration_la': [0, 1, 2, 3, 5],
        'market_penetration_asia': [0, 0, 1, 2, 3],
        'roi_percentage': [0, 5, 12, 18, 22],
        'revenue_millions': [0, 25, 75, 150, 250],
        'cumulative_investment': [25000000, 50000000, 100000000, 150000000, 225000000],
        'phase': ['Phase 1', 'Phase 1', 'Phase 2', 'Phase 2', 'Phase 3']
    }
    return pd.DataFrame(data)

def create_risk_analysis():
    """Create risk analysis data"""
    data = {
        'risk_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'risk_category': [
            'Geopolitical', 'Economic', 'Operational', 'Market', 'Financial',
            'Technology', 'Cultural', 'Logistics', 'Regulatory', 'Competition'
        ],
        'risk_description': [
            'Regulatory changes in target markets',
            'Currency fluctuations affecting profitability',
            'Supply chain disruptions',
            'Competition from local players',
            'Investment cost overruns',
            'Digital infrastructure challenges',
            'Market acceptance of products',
            'Distribution network delays',
            'Food safety regulations',
            'Price wars with competitors'
        ],
        'probability': ['Medium', 'High', 'Medium', 'High', 'Medium', 'Low', 'Medium', 'Medium', 'Low', 'High'],
        'impact': ['High', 'Medium', 'High', 'Medium', 'High', 'Medium', 'Medium', 'Medium', 'High', 'High'],
        'mitigation_strategy': [
            'Diversify across multiple regions',
            'Hedge currency exposure',
            'Establish multiple suppliers',
            'Focus on premium positioning',
            'Conservative budgeting and monitoring',
            'Partner with local tech providers',
            'Extensive market research',
            'Early establishment of logistics',
            'Compliance with local standards',
            'Differentiation through quality'
        ],
        'phase_affected': [
            'All Phases', 'All Phases', 'Phase 2', 'Phase 1', 'All Phases',
            'Phase 3', 'Phase 1', 'Phase 1', 'All Phases', 'Phase 2'
        ]
    }
    return pd.DataFrame(data)

def create_organizational_structure():
    """Create organizational structure data"""
    data = {
        'department_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
        'department_name': [
            'Company', 'Engineering', 'Product', 'Sales', 'Operations',
            'Backend', 'Frontend', 'Mobile', 'DevOps', 'Design',
            'Product Management', 'Analytics', 'Enterprise', 'SMB', 'Partnerships',
            'HR', 'Finance', 'Legal', 'IT'
        ],
        'parent_department': [
            'Root', 'Company', 'Company', 'Company', 'Company',
            'Engineering', 'Engineering', 'Engineering', 'Engineering', 'Product',
            'Product', 'Product', 'Sales', 'Sales', 'Sales',
            'Operations', 'Operations', 'Operations', 'Operations'
        ],
        'employee_count': [500, 180, 80, 120, 120, 60, 50, 40, 30, 30, 25, 25, 50, 40, 30, 40, 35, 25, 20],
        'budget_allocation': [
            56800000, 21600000, 8800000, 15600000, 10800000,
            6000000, 5000000, 4000000, 3000000, 3000000,
            2500000, 2500000, 6500000, 5200000, 3900000,
            3600000, 3150000, 2250000, 1800000
        ],
        'role_description': [
            'Overall company structure',
            'Technical development and infrastructure',
            'Product management and development',
            'Sales and customer acquisition',
            'Operational management and logistics',
            'Backend development and APIs',
            'Frontend development and UI/UX',
            'Mobile application development',
            'DevOps and infrastructure management',
            'Design and user experience',
            'Product strategy and roadmap',
            'Data analytics and insights',
            'Enterprise sales and partnerships',
            'Small and medium business sales',
            'Strategic partnerships and alliances',
            'Human resources and talent management',
            'Financial management and accounting',
            'Legal and compliance',
            'Information technology support'
        ]
    }
    return pd.DataFrame(data)

def create_market_analysis():
    """Create market analysis data"""
    data = {
        'country_name': ['Brazil', 'Mexico', 'Argentina', 'Chile', 'China', 'India', 'Indonesia', 'Vietnam', 'Colombia', 'Peru', 'Thailand', 'Malaysia'],
        'continent': ['Americas', 'Americas', 'Americas', 'Americas', 'Asia', 'Asia', 'Asia', 'Asia', 'Americas', 'Americas', 'Asia', 'Asia'],
        'population': [211998573, 130861007, 45696159, 19764771, 1408975000, 1450935791, 283487931, 100987686, 52886363, 34217848, 71668011, 35557673],
        'gdp_per_capita': [10280.31, 14157.94, 13858.20, 16709.89, 13303.15, 2696.66, 4925.43, 4717.29, 7913.99, 8452.37, 7345.14, 11867.26],
        'gdp_total': [2179000000000, 1853000000000, 633000000000, 330000000000, 18740000000000, 3910000000000, 1395000000000, 476000000000, 418000000000, 289000000000, 526000000000, 422000000000],
        'market_type': ['Premium', 'Premium', 'Premium', 'Premium', 'Volume', 'Volume', 'Volume', 'Volume', 'Premium', 'Premium', 'Volume', 'Volume'],
        'priority_level': [1, 1, 2, 2, 1, 1, 2, 2, 3, 3, 3, 3],
        'market_opportunity_score': [85, 82, 75, 78, 95, 88, 72, 68, 65, 62, 70, 73],
        'population_percentage': [2.7, 1.7, 0.6, 0.3, 18.3, 18.8, 3.7, 1.3, 0.7, 0.4, 0.9, 0.5],
        'gdp_percentage': [1.7, 1.4, 0.5, 0.3, 14.7, 3.1, 1.1, 0.4, 0.3, 0.2, 0.4, 0.3]
    }
    return pd.DataFrame(data)

def main():
    """Generate Excel file with all tables"""
    
    # Create Excel writer
    with pd.ExcelWriter('TCF_Strategic_Dashboard_Tables.xlsx', engine='openpyxl') as writer:
        
        # Create all dataframes
        implementation_phases = create_implementation_phases()
        priority_countries = create_priority_countries()
        implementation_tasks = create_implementation_tasks()
        financial_metrics = create_financial_metrics()
        kpi_projections = create_kpi_projections()
        risk_analysis = create_risk_analysis()
        organizational_structure = create_organizational_structure()
        market_analysis = create_market_analysis()
        
        # Write each dataframe to a separate sheet
        implementation_phases.to_excel(writer, sheet_name='Implementation_Phases', index=False)
        priority_countries.to_excel(writer, sheet_name='Priority_Countries', index=False)
        implementation_tasks.to_excel(writer, sheet_name='Implementation_Tasks', index=False)
        financial_metrics.to_excel(writer, sheet_name='Financial_Metrics', index=False)
        kpi_projections.to_excel(writer, sheet_name='KPI_Projections', index=False)
        risk_analysis.to_excel(writer, sheet_name='Risk_Analysis', index=False)
        organizational_structure.to_excel(writer, sheet_name='Organizational_Structure', index=False)
        market_analysis.to_excel(writer, sheet_name='Market_Analysis', index=False)
        
        # Create summary sheet
        summary_data = {
            'Table_Name': [
                'Implementation_Phases',
                'Priority_Countries', 
                'Implementation_Tasks',
                'Financial_Metrics',
                'KPI_Projections',
                'Risk_Analysis',
                'Organizational_Structure',
                'Market_Analysis'
            ],
            'Description': [
                'Strategic implementation phases with objectives and actions',
                'Priority countries for TCF expansion with market data',
                'Detailed task timeline for implementation',
                'Financial metrics and targets for each phase',
                'KPI projections over 5-year period',
                'Risk assessment and mitigation strategies',
                'TCF organizational structure and budget allocation',
                'Market opportunity analysis by country'
            ],
            'Records': [
                len(implementation_phases),
                len(priority_countries),
                len(implementation_tasks),
                len(financial_metrics),
                len(kpi_projections),
                len(risk_analysis),
                len(organizational_structure),
                len(market_analysis)
            ],
            'Key_Fields': [
                'phase_name, investment_amount, objectives, actions',
                'country_name, market_type, priority_level, gdp_total',
                'task_name, start_date, end_date, phase, investment_amount',
                'metric_name, value, unit, target_year',
                'year, roi_percentage, revenue_millions, market_penetration',
                'risk_category, probability, impact, mitigation_strategy',
                'department_name, employee_count, budget_allocation',
                'country_name, market_opportunity_score, population, gdp_per_capita'
            ]
        }
        
        summary_df = pd.DataFrame(summary_data)
        summary_df.to_excel(writer, sheet_name='Summary', index=False)
    
    print("✅ Excel file 'TCF_Strategic_Dashboard_Tables.xlsx' created successfully!")
    print("\n📊 Tables included:")
    print("1. Implementation_Phases - Strategic phases with objectives and actions")
    print("2. Priority_Countries - Countries with market data and priority levels")
    print("3. Implementation_Tasks - Detailed task timeline")
    print("4. Financial_Metrics - Financial targets and metrics")
    print("5. KPI_Projections - 5-year projections")
    print("6. Risk_Analysis - Risk assessment and mitigation")
    print("7. Organizational_Structure - TCF structure and budgets")
    print("8. Market_Analysis - Market opportunity analysis")
    print("9. Summary - Overview of all tables")

if __name__ == "__main__":
    main()
