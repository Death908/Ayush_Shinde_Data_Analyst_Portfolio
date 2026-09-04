# Ayush Shinde — Data Analyst Portfolio

## E-Commerce Sales Performance Analysis

[![SQL](https://img.shields.io/badge/SQL-Analysis-blue)](sql/ecommerce_sales_analysis.sql) [![Python](https://img.shields.io/badge/Python-Pandas%2FNumPy-yellow)](python/ecommerce_sales_analysis.py) [![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-orange)](powerbi/dax_measures.md) [![Excel](https://img.shields.io/badge/Excel-Data%20Cleaning-green)](data/README.md)

An end-to-end **Data Analyst portfolio project** demonstrating a complete workflow from imperfect transaction data to business-focused analysis and dashboard design.

> **Dataset note:** This is a synthetic dataset created for learning and portfolio purposes. It is not presented as real company data.

## Business Objective
Analyze e-commerce sales performance and identify patterns in revenue, profit, orders, products, regions, categories, and sales channels that can support business decisions.

## Tools
- **Excel:** data cleaning, transformation, KPI summaries and reporting
- **SQL:** KPI calculations and multidimensional analysis
- **Python:** Pandas/NumPy cleaning and exploratory analysis
- **Power BI:** interactive KPI dashboard, trends, rankings and slicers

## Workflow
**Raw Data → Data Cleaning → Validation → EDA → SQL Analysis → Power BI → Insights & Recommendations**

## Dataset
The cleaned analytical dataset contains **1,200 records and 14 columns** covering orders, dates, region, sales channel, category, product, units sold, price, discount, revenue, cost, profit, month and profit margin.

The raw data intentionally includes duplicates and missing categorical values so the project demonstrates real-world data-quality handling.

See [`data/README.md`](data/README.md) for the data dictionary and cleaning notes.

## Key Analysis
The project answers:
1. What are total revenue, profit, orders and units sold?
2. How does revenue and profit change over time?
3. Which categories and products contribute most?
4. Which regions perform best?
5. Which sales channel generates the most revenue?
6. Where are opportunities to improve profitability?

## Power BI Dashboard
The dashboard specification includes:
- Total Revenue
- Total Profit
- Total Orders
- Units Sold
- Profit Margin
- Average Order Value
- Monthly Revenue & Profit trend
- Category performance
- Regional revenue
- Sales-channel performance
- Top 10 products by revenue
- Date, Region, Category and Sales Channel slicers

See [`powerbi/dax_measures.md`](powerbi/dax_measures.md).

## SQL
The SQL analysis includes overall KPIs, monthly trends, regional performance, category performance, top products and sales-channel analysis.

See [`sql/ecommerce_sales_analysis.sql`](sql/ecommerce_sales_analysis.sql).

## Python
The Python workflow documents the Pandas/NumPy approach for duplicate removal, categorical standardization, KPI calculation and grouped analysis.

See [`python/ecommerce_sales_analysis.py`](python/ecommerce_sales_analysis.py).

## Repository Structure
```text
.
├── README.md
├── data/
│   └── README.md
├── sql/
│   └── ecommerce_sales_analysis.sql
├── python/
│   └── ecommerce_sales_analysis.py
└── powerbi/
    └── dax_measures.md
```

## Analyst Skills Demonstrated
**Data Cleaning · Data Validation · SQL · Excel · Python · Pandas · NumPy · Power BI · DAX · KPI Analysis · EDA · Dashboard Design · Business Insights**

## Portfolio Note
This project is designed to demonstrate how a junior analyst can structure a complete analytical problem: define KPIs, clean imperfect data, validate calculations, investigate business dimensions, build a decision-focused dashboard, and communicate recommendations clearly.
