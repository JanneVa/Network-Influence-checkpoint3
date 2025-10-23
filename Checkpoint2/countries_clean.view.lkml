view: countries {
  sql_table_name: `your_project.your_dataset.looker_countries_clean` ;;
  
  dimension: country_id {
    type: number
    primary_key: yes
    sql: ${TABLE}.country_id ;;
  }
  
  dimension: country_name {
    type: string
    sql: ${TABLE}.country_name ;;
    label: "Country"
  }
  
  dimension: continent {
    type: string
    sql: ${TABLE}.continent ;;
    label: "Continent"
  }
  
  dimension: market_type {
    type: string
    sql: ${TABLE}.market_type ;;
    label: "Market Type"
  }
  
  dimension: priority_level {
    type: number
    sql: ${TABLE}.priority_level ;;
    label: "Priority Level"
  }
  
  dimension: region {
    type: string
    sql: ${TABLE}.region ;;
    label: "Region"
  }
  
  dimension: population {
    type: number
    sql: ${TABLE}.population ;;
    label: "Population"
    value_format_name: decimal_0
  }
  
  dimension: population_millions {
    type: number
    sql: ${TABLE}.population_millions ;;
    label: "Population (Millions)"
    value_format_name: decimal_1
  }
  
  dimension: gdp_per_capita {
    type: number
    sql: ${TABLE}.gdp_per_capita ;;
    label: "GDP per Capita"
    value_format_name: usd
  }
  
  dimension: gdp_total {
    type: number
    sql: ${TABLE}.gdp_total ;;
    label: "Total GDP"
    value_format_name: usd
  }
  
  dimension: gdp_billions {
    type: number
    sql: ${TABLE}.gdp_billions ;;
    label: "GDP (Billions)"
    value_format_name: decimal_0
  }
  
  dimension: market_opportunity_score {
    type: number
    sql: ${TABLE}.market_opportunity_score ;;
    label: "Market Opportunity Score"
    value_format_name: decimal_0
  }
  
  measure: total_population {
    type: sum
    sql: ${TABLE}.population ;;
    label: "Total Population"
    value_format_name: decimal_0
  }
  
  measure: avg_gdp_per_capita {
    type: average
    sql: ${TABLE}.gdp_per_capita ;;
    label: "Average GDP per Capita"
    value_format_name: usd
  }
  
  measure: total_gdp {
    type: sum
    sql: ${TABLE}.gdp_total ;;
    label: "Total GDP"
    value_format_name: usd
  }
  
  measure: avg_market_opportunity_score {
    type: average
    sql: ${TABLE}.market_opportunity_score ;;
    label: "Average Market Opportunity Score"
    value_format_name: decimal_1
  }
  
  measure: count_countries {
    type: count
    sql: ${TABLE}.country_id ;;
    label: "Number of Countries"
  }
}
