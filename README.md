# Ayush Shinde — Data Analyst Portfolio

## E-Commerce Sales Performance Analysis

An end-to-end portfolio project demonstrating practical data analysis using **Excel, SQL, Python (Pandas/NumPy), and Power BI**.

> **Dataset note:** This is a synthetic dataset created for learning and portfolio purposes. It is not presented as real company data.

### Business Objective
Analyze e-commerce sales performance and convert transaction-level data into actionable insights across revenue, profit, orders, products, regions, categories, and sales channels.

### Tools & Skills
- Excel — cleaning, transformation, KPI summaries, reporting
- SQL — KPI calculations and multidimensional analysis
- Python — Pandas/NumPy cleaning and exploratory analysis
- Power BI — KPI dashboard, trends, rankings, slicers

### Workflow
**Raw Data → Data Cleaning → EDA → SQL Analysis → Power BI Dashboard → Business Insights**

### Dashboard
The Power BI dashboard is designed as an executive sales overview covering:
- Total Revenue, Total Profit, Total Orders, Units Sold
- Profit Margin and Average Order Value
- Monthly Revenue & Profit trend
- Revenue & Profit by Category
- Revenue by Region
- Revenue by Sales Channel
- Top 10 Products by Revenue
- Interactive Date, Region, Category, and Sales Channel filters

### Core DAX Measures
```DAX
Total Revenue = SUM(Cleaned_Data[Revenue])
Total Profit = SUM(Cleaned_Data[Profit])
Total Orders = DISTINCTCOUNT(Cleaned_Data[Order_ID])
Units Sold = SUM(Cleaned_Data[Units_Sold])
Profit Margin = DIVIDE([Total Profit], [Total Revenue], 0)
Average Order Value = DIVIDE([Total Revenue], [Total Orders], 0)
```

### Analytical Questions
1. How much revenue and profit did the business generate?
2. How does performance change month over month?
3. Which categories and products contribute most to revenue and profit?
4. Which regions perform best?
5. Which sales channel contributes most to revenue?
6. Where are opportunities to improve profitability?

### Repository Structure
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

### Portfolio Focus
This project emphasizes practical analyst thinking: defining KPIs, cleaning imperfect data, validating calculations, analyzing business dimensions, designing decision-focused dashboards, and translating findings into recommendations.
