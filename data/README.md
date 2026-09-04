# Data

## Source
Synthetic e-commerce transaction dataset created for portfolio and learning purposes.

## Dataset Design
- Raw records: 1,212
- Cleaned records: 1,200
- Intentional data-quality issues include duplicate rows and missing categorical values.

## Main Fields
`Order_ID`, `Order_Date`, `Region`, `Sales_Channel`, `Category`, `Product`, `Units_Sold`, `Unit_Price`, `Discount`, `Revenue`, `Cost`, `Profit`, `Month`, `Profit_Margin`

## Cleaning Approach
1. Identify duplicate records.
2. Handle missing categorical values.
3. Standardize categorical values.
4. Validate revenue, cost, profit and margin fields.
5. Produce a cleaned analysis-ready dataset.

The full Excel workbook containing Raw_Data and Cleaned_Data is maintained as the project source file outside this repository when binary-file storage is not required.
