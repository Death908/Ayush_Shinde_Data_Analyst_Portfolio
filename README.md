# Ayush Shinde — Data Analyst Portfolio

## E-Commerce Sales Performance Analysis

[![SQL](https://img.shields.io/badge/SQL-Analysis-blue)](sql/ecommerce_sales_analysis.sql) [![Python](https://img.shields.io/badge/Python-Pandas%2FNumPy-yellow)](python/ecommerce_sales_analysis.py) [![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-orange)](powerbi/dax_measures.md) [![Excel](https://img.shields.io/badge/Excel-Data%20Cleaning-green)](data/README.md)

An end-to-end **Data Analyst portfolio project** demonstrating how raw transaction data can be cleaned, validated, analyzed and converted into business-focused KPIs, insights and a Power BI dashboard design.

> **Portfolio dataset note:** This dataset is created for portfolio and learning purposes. It is not presented as data from a real company.

## 🎯 Business Objective
Analyze e-commerce sales performance across time, products, categories, regions and sales channels to identify revenue and profitability patterns and support data-driven recommendations.

## 🛠️ Tools & Skills
- **Excel:** cleaning, transformation, KPI reporting and validation
- **SQL:** aggregations, KPI calculations, grouping, ranking and trend analysis
- **Python:** Pandas/NumPy data preparation and exploratory analysis
- **Power BI:** dashboard design, KPI cards, trends, slicers and business reporting
- **Analytics:** data quality checks, EDA, profitability analysis and recommendations

## 🔄 Analytical Workflow
**Raw Data → Data Cleaning → Validation → EDA → SQL Analysis → Power BI → Insights & Recommendations**

## 📊 Dashboard Preview

![E-Commerce Sales Performance Dashboard](powerbi_dashboard.png)

The dashboard design focuses on the questions a business stakeholder would typically ask:
- How much revenue and profit are we generating?
- How is performance changing month over month?
- Which categories and products drive revenue?
- Which regions and channels perform best?
- Where should management investigate profitability opportunities?

## 📈 Key Results
Based on the cleaned portfolio dataset:

| KPI | Result |
|---|---:|
| Total Revenue | ₹12,583,439 |
| Total Profit | ₹3,789,315 |
| Profit Margin | 30.1% |
| Orders | 1,200 |
| Units Sold | 5,364 |
| Average Order Value | ₹10,486 |

### Key Findings
1. **West** generated the highest revenue among regions.
2. **Electronics** was the highest-revenue category.
3. **Storage Set** was the top product by revenue.
4. **Website** generated the highest revenue among sales channels.

See [`INSIGHTS.md`](INSIGHTS.md) for the business interpretation and recommendations.

## 🧹 Data Quality & Cleaning
The raw dataset intentionally contains source-style quality issues, including duplicate records and missing categorical values. The project demonstrates:

- Duplicate detection and removal
- Missing-value identification and handling
- Categorical standardization
- Calculated-field validation
- KPI reconciliation across analysis steps

The raw and cleaned datasets are available in [`data/`](data/).

## 🧮 SQL Analysis
The SQL layer covers:

- Overall revenue, profit, orders and units sold
- Average order value and profit margin
- Monthly revenue and profit trends
- Regional performance
- Category performance
- Top products by revenue
- Sales-channel performance

See [`sql/ecommerce_sales_analysis.sql`](sql/ecommerce_sales_analysis.sql).

## 🐍 Python Analysis
The Python workflow demonstrates a practical Pandas/NumPy approach to:

- Load and inspect transaction data
- Detect duplicate records
- Handle missing categorical values
- Standardize fields
- Calculate KPIs
- Perform grouped analysis for business dimensions

See [`python/ecommerce_sales_analysis.py`](python/ecommerce_sales_analysis.py).

## 📊 Power BI
The Power BI specification includes DAX measures for:

- Total Revenue
- Total Profit
- Total Orders
- Units Sold
- Profit Margin
- Average Order Value
- Previous-month revenue/profit
- Month-over-month growth

Recommended dashboard views include KPI cards, monthly trends, category performance, regional revenue, sales-channel performance, top products and interactive slicers.

See [`powerbi/dax_measures.md`](powerbi/dax_measures.md).

## 📁 Repository Structure
```text
.
├── README.md
├── INSIGHTS.md
├── powerbi_dashboard.png
├── data/
│   ├── README.md
│   ├── ecommerce_sales_raw.csv
│   └── ecommerce_sales_cleaned.csv
├── sql/
│   └── ecommerce_sales_analysis.sql
├── python/
│   └── ecommerce_sales_analysis.py
└── powerbi/
    └── dax_measures.md
```

## 💡 Analyst Skills Demonstrated
**Data Cleaning · Data Validation · SQL · Excel · Python · Pandas · NumPy · Power BI · DAX · KPI Analysis · EDA · Dashboard Design · Business Insights**

## 👤 About This Project
This project is designed to demonstrate a junior Data Analyst workflow from imperfect source data to a decision-focused analytical output. The emphasis is not only on calculating numbers, but also on validating the data, structuring analysis around business questions and communicating actionable findings.
