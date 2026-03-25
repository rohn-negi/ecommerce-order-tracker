from sqlalchemy import create_engine, text
import pandas as pd


engine = create_engine("mysql+mysqlconnector://root:@localhost/school", echo=False)

df = pd.read_sql(text("SELECT * FROM orders_ecom"), engine)

print("FULL TABLE")
print(df)

print(f"\n Total revenue generated : {df['total_price'].sum()}")


msp = pd.read_sql(text("""
    SELECT product_id, COUNT(*) as total_orders
    FROM orders_ecom
    GROUP BY product_id
    ORDER BY total_orders DESC
"""), engine)

print(f"\n  Most ordered product : {msp}")


ryos = pd.read_sql(text("""
    SELECT status, SUM(total_price) AS REVENUE
    FROM orders_ecom 
    GROUP BY status
"""), engine)

print(f"\n  Revenue by order status : {ryos}")

hsc = pd.read_sql(text("""
    SELECT customer_id, SUM(total_price ) AS totalSpent
    FROM orders_ecom 
    GROUP BY customer_id
    ORDER BY totalSpent DESC
"""), engine)

print(f"\n  Highest spending customer : {hsc}")


customerAndPr = pd.read_sql(text("""
    SELECT 
        c.name AS customer_name, 
        p.name AS product_name, 
        o.quantity, 
        o.status
    FROM orders_ecom o
    JOIN customers_ecom c ON o.customer_id = c.id
    JOIN products_ecom  p ON o.product_id  = p.id
"""), engine)

print(f"\n{customerAndPr}")