import pandas as pd
import matplotlib.pyplot as plt

# Load processed data
monthly_sales = pd.read_csv('reports/monthly_revenue.csv')
df = pd.read_csv('data/clean_sales.csv')

# KPI: Top Products
top_products = df.groupby('Product').agg({'Revenue': 'sum'}).sort_values(by='Revenue', ascending=False).head(10)

# KPI: Revenue by Region
region_sales = df.groupby('Region').agg({'Revenue': 'sum'}).reset_index()

# Monthly Revenue Trend
plt.figure(figsize=(8,5))
plt.plot(monthly_sales['Order Date'], monthly_sales['Revenue'], marker='o')
plt.title('Monthly Revenue Trend')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.grid(True)
plt.tight_layout()
plt.savefig('reports/monthly_revenue_trend.png')
plt.close()

# Top Products
plt.figure(figsize=(8,5))
plt.bar(top_products.index, top_products['Revenue'])
plt.title('Top 10 Products by Revenue')
plt.xticks(rotation=45)
plt.ylabel('Revenue')
plt.tight_layout()
plt.savefig('reports/top_products.png')
plt.close()

# Revenue by Region
plt.figure(figsize=(6,4))
plt.bar(region_sales['Region'], region_sales['Revenue'], color='orange')
plt.title('Revenue by Region')
plt.ylabel('Revenue')
plt.tight_layout()
plt.savefig('reports/revenue_by_region.png')
plt.close()

print('Visualizations created and saved in reports/.')
