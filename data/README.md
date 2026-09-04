# E-Commerce Sales Performance Dataset

## Dataset Overview
The **E-Commerce Sales Performance Dataset** is the transaction dataset used for this portfolio project. It is structured to demonstrate practical Data Analyst skills including data cleaning, validation, KPI analysis and business reporting.

> **Portfolio note:** The dataset is created for portfolio and learning purposes and is not presented as data from a real company.

## Files
- `ecommerce_sales_raw.csv` — source-style transaction data containing data-quality issues
- `ecommerce_sales_cleaned.csv` — cleaned analytical dataset used for analysis
- `Ecommerce_Sales_Data_Analyst_Project.xlsx` — earlier workbook version containing raw, cleaned and analysis sheets

## Dataset Structure
The cleaned dataset contains **1,200 records and 14 analytical fields**:

- `Order_ID` — unique order identifier
- `Order_Date` — transaction date
- `Region` — sales region
- `Sales_Channel` — Website, Marketplace or Mobile App
- `Category` — product category
- `Product` — product name
- `Units_Sold` — quantity sold
- `Unit_Price` — price per unit
- `Discount` — applied discount rate
- `Revenue` — net sales revenue after discount
- `Cost` — estimated cost associated with the transaction
- `Profit` — revenue minus cost
- `Month` — month derived from order date
- `Profit_Margin` — profit as a percentage of revenue

## Data-Quality Workflow
The source-style dataset includes duplicate records and missing categorical values. The cleaning workflow demonstrates:

1. Duplicate detection and removal
2. Missing-value identification and handling
3. Categorical value standardization
4. Calculated-field validation
5. KPI reconciliation between Excel, SQL and Python

## Analytical Use
The dataset supports analysis of revenue and profit trends, regional performance, category performance, product rankings, sales-channel performance, profitability and KPI movement.

## Tools Used
**Excel · SQL · Python · Pandas · NumPy · Power BI**
