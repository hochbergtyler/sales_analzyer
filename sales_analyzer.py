import csv

# Read the CSV
sales = []
with open('sales_data.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        row['quantity'] = int(row['quantity'])
        row['price'] = float(row['price'])
        sales.append(row)

print(f"Loaded {len(sales)} sales records")

# Calculate total revenue
total_revenue = sum(sale["quantity"] * sale["price"] for sale in sales)
print(f"Total Revenue: ${total_revenue:.2f}")

# Revenue by product
revenue_by_product = {}
for sale in sales:
    product = sale["product"]
    revenue = sale["quantity"] * sale["price"]
    if product not in revenue_by_product:
        revenue_by_product[product] = 0
    revenue_by_product[product] += revenue

print("\nRevenue by Product:")
for product, revenue in sorted(revenue_by_product.items()):
    print(f"  {product}: ${revenue:.2f}")

# Quantity by product
quantity_by_product = {}
for sale in sales:
    product = sale["product"]
    quantity = sale["quantity"]
    if product not in quantity_by_product:
        quantity_by_product[product] = 0
    quantity_by_product[product] += quantity

print("\nQuantity by Product:")
for product, qty in sorted(quantity_by_product.items()):
    print(f"  {product}: {qty}")

# Day with highest revenue
daily_revenue = {}
for sale in sales:
    date = sale["date"]
    revenue = sale["quantity"] * sale["price"]
    if date not in daily_revenue:
        daily_revenue[date] = 0
    daily_revenue[date] += revenue

max_day = max(daily_revenue, key=daily_revenue.get)
print(f"\nDay with Highest Revenue: {max_day} (${daily_revenue[max_day]:.2f})")

# === Write to files as required ===

# sales_report.txt
with open('sales_report.txt', 'w') as f:
    f.write("Sales Analysis Report\n")
    f.write("============================\n\n")
    f.write(f"Total Revenue: ${total_revenue:.2f}\n\n")
    f.write("Revenue by Product:\n")
    for product, revenue in sorted(revenue_by_product.items()):
        f.write(f"  {product}: ${revenue:.2f}\n")
    f.write("\nQuantity by Product:\n")
    for product, qty in sorted(quantity_by_product.items()):
        f.write(f"  {product}: {qty}\n")
    f.write(f"\nDay with Highest Revenue: {max_day} (${daily_revenue[max_day]:.2f})\n")

# product_summary.csv
with open('product_summary.csv', 'w') as f:
    f.write("product,total_quantity,total_revenue\n")
    for product in sorted(revenue_by_product):
        f.write(f"{product},{quantity_by_product[product]},{revenue_by_product[product]:.2f}\n")

print("\nFiles written: sales_report.txt and product_summary.csv") 
