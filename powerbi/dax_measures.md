# Power BI — DAX Measures & Build Specification

## Core Measures

```DAX
Total Revenue = SUM(Cleaned_Data[Revenue])
Total Profit = SUM(Cleaned_Data[Profit])
Total Orders = DISTINCTCOUNT(Cleaned_Data[Order_ID])
Units Sold = SUM(Cleaned_Data[Units_Sold])
Profit Margin = DIVIDE([Total Profit], [Total Revenue], 0)
Average Order Value = DIVIDE([Total Revenue], [Total Orders], 0)
```

## Date Table

```DAX
Date = CALENDAR(MIN(Cleaned_Data[Order_Date]), MAX(Cleaned_Data[Order_Date]))

Year = YEAR('Date'[Date])
Month Number = MONTH('Date'[Date])
Month = FORMAT('Date'[Date], "MMM")
Year Month = FORMAT('Date'[Date], "YYYY-MM")
```

Sort `Month` by `Month Number`, mark `Date` as the date table, and create a one-to-many relationship from `Date[Date]` to `Cleaned_Data[Order_Date]`.

## MoM Measures

```DAX
Revenue Previous Month =
CALCULATE([Total Revenue], DATEADD('Date'[Date], -1, MONTH))

Revenue MoM % =
DIVIDE([Total Revenue] - [Revenue Previous Month], [Revenue Previous Month], 0)

Profit Previous Month =
CALCULATE([Total Profit], DATEADD('Date'[Date], -1, MONTH))

Profit MoM % =
DIVIDE([Total Profit] - [Profit Previous Month], [Profit Previous Month], 0)
```

## Page 1 — Executive Sales Overview
- KPI cards: Revenue, Profit, Orders, Units Sold
- Monthly Revenue & Profit trend
- Revenue & Profit by Category
- Revenue by Region
- Revenue by Sales Channel
- Top 10 Products by Revenue
- Slicers: Date, Region, Category, Sales Channel

## Page 2 — Product & Category Analysis
- Product ranking
- Revenue vs Profit comparison
- Category contribution
- Units sold and margin analysis

## Page 3 — Regional & Channel Analysis
- Regional revenue/profit
- Sales-channel performance
- KPI comparison and drill-downs

## Design Goal
Keep the report executive-friendly: clear KPI hierarchy, limited visual clutter, consistent number formatting, meaningful titles, and interactive slicers that support business questions.
