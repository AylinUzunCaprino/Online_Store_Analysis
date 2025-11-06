import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("data/store_sales.csv")

# Create a new column for total sales
df["total_sales"] = df["quantity"] * df["unit_price"]

# Convert order_date column to datetime and extract month
df["order_date"] = pd.to_datetime(df["order_date"])
df["month"] = df["order_date"].dt.to_period("M")

# Group by month to calculate total sales and profit
monthly = df.groupby("month")[["total_sales", "profit"]].sum().reset_index()

# Group by category to find top-selling product categories
category_sales = df.groupby("category")["total_sales"].sum().sort_values(ascending=False)

# Group by region to find best-performing regions
region_sales = df.groupby("region")["total_sales"].sum().sort_values(ascending=False)

# Print key results
print("Monthly Sales & Profit:")
print(monthly)
print("\nSales by Category:")
print(category_sales)
print("\nSales by Region:")
print(region_sales)

# Plot a trend of sales and profit over time
plt.plot(monthly["month"].astype(str), monthly["total_sales"], marker="o", label="Sales")
plt.plot(monthly["month"].astype(str), monthly["profit"], marker="s", label="Profit")
plt.title("Monthly Sales & Profit Trend")
plt.xlabel("Month")
plt.ylabel("Amount ($)")
plt.legend()
plt.tight_layout()
plt.show()
