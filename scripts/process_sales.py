import pandas as pd

# Load raw data
df = pd.read_csv('data/raw_sales.csv')

# Data Cleaning
df.dropna(inplace=True)
df['Order Date'] = pd.to_datetime(df['Order Date'])
df.drop_duplicates(inplace=True)

# KPI Calculations
df['Revenue'] = df['Quantity'] * df['Unit Price']
monthly_sales = df.groupby(df['Order Date'].dt.to_period('M')).agg({'Revenue': 'sum'}).reset_index()
monthly_sales['Order Date'] = monthly_sales['Order Date'].astype(str)

# Save outputs
df.to_csv('data/clean_sales.csv', index=False)
monthly_sales.to_csv('reports/monthly_revenue.csv', index=False)

print('Data processing complete. Clean data and KPI reports saved.')
