# E-Commerce Order Tracker

A Python + MySQL project that simulates a real e-commerce order management system.

## Tech Stack
- Python 3
- MySQL (via XAMPP)
- SQLAlchemy ORM
- Pandas

## Project Structure
- `Database.py` — defines Customers, Products and Orders tables using SQLAlchemy ORM
- `Insert.py` — inserts sample data (10 customers, 10 products, 10 orders)
- `Analysis.py` — business insights using Pandas + SQL queries

## Business Insights Generated
- Total revenue
- Revenue by order status
- Highest spending customer
- Most ordered product
- Full order details with customer and product names (JOIN)

## How to Run
1. Install dependencies:
   pip install -r requirements.txt
2. Start MySQL via XAMPP
3. Run database.py to create tables
4. Run insert.py to populate data
5. Run analysis.py to see insights

## Database Schema
- Customers → id, name, email (unique), city
- Products  → id, name, category, price, stock
- Orders    → id, customer_id (FK), product_id (FK), quantity, total_price, order_date, status
`





