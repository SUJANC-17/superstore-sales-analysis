import pandas as pd
import numpy as np

# Load data
df = pd.read_csv(r'D:\Data Analyst\train.csv')

# Convert dates
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)
df['Ship Date'] = pd.to_datetime(df['Ship Date'], dayfirst=True)
df['Shipping Days'] = (df['Ship Date'] - df['Order Date']).dt.days

# 1. Regional Analysis
print("=== REGIONAL SALES ===")
print(df.groupby('Region')['Sales'].sum().sort_values(ascending=False))

# 2. Category Analysis
print("\n=== CATEGORY ANALYSIS ===")
print(df.groupby('Category').agg({'Sales': ['sum', 'count']}))

# 3. Top 10 Customers
print("\n=== TOP 10 CUSTOMERS ===")
print(df.groupby('Customer ID')['Sales'].sum().sort_values(ascending=False).head(10))

# 4. Monthly Sales
print("\n=== MONTHLY SALES ===")
print(df.groupby(df['Order Date'].dt.month)['Sales'].sum().sort_values(ascending=False))

# 5. Shipping Correlation
print("\n=== SHIPPING VS SALES CORRELATION ===")
print(df[['Sales', 'Shipping Days']].corr())