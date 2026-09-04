"""E-Commerce Sales Performance Analysis
Synthetic portfolio dataset.

Expected input columns:
Order_ID, Order_Date, Region, Sales_Channel, Category, Product,
Units_Sold, Unit_Price, Discount, Revenue, Cost, Profit
"""

import pandas as pd
import numpy as np


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean duplicates, standardize categorical fields and prepare analysis columns."""
    df = df.copy()
    df = df.drop_duplicates().reset_index(drop=True)

    categorical_cols = ["Region", "Sales_Channel", "Category", "Product"]
    for col in categorical_cols:
        df[col] = df[col].fillna("Unknown").astype(str).str.strip()

    df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")
    df["Month"] = df["Order_Date"].dt.to_period("M").astype(str)

    # Recalculate derived measures for validation.
    df["Revenue_Calculated"] = (
        df["Units_Sold"] * df["Unit_Price"] * (1 - df["Discount"])
    )
    df["Profit_Calculated"] = df["Revenue_Calculated"] - df["Cost"]
    df["Profit_Margin"] = np.where(
        df["Revenue_Calculated"] != 0,
        df["Profit_Calculated"] / df["Revenue_Calculated"],
        0,
    )
    return df


def summarize(df: pd.DataFrame) -> dict:
    """Return portfolio KPI summary."""
    return {
        "total_revenue": df["Revenue"].sum(),
        "total_profit": df["Profit"].sum(),
        "total_orders": df["Order_ID"].nunique(),
        "units_sold": df["Units_Sold"].sum(),
        "average_order_value": df["Revenue"].sum() / df["Order_ID"].nunique(),
        "profit_margin": df["Profit"].sum() / df["Revenue"].sum(),
    }


if __name__ == "__main__":
    # Replace with the path to Cleaned_Data exported from the project workbook.
    input_file = "Cleaned_Data.csv"
    df = pd.read_csv(input_file)
    cleaned = clean_data(df)
    print(summarize(cleaned))

    print("\nTop categories by revenue:")
    print(cleaned.groupby("Category")["Revenue"].sum().sort_values(ascending=False))

    print("\nTop products by revenue:")
    print(cleaned.groupby("Product")["Revenue"].sum().sort_values(ascending=False).head(10))
