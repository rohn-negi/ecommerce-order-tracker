from sqlalchemy.orm import Session
from datetime import date

from Database import engine, Customer, Product, Order

session = Session(engine)

# Add customers
customers = [
    Customer(name="Rahul Sharma", email="rahul.sharma@gmail.com", city="Delhi"),
    Customer(name="Priya Verma", email="priya.verma@gmail.com", city="Mumbai"),
    Customer(name="Amit Singh", email="amitt.singh@gmail.com", city="Lucknow"),
    Customer(name="Neha Gupta", email="neha.gupta@gmail.com", city="Jaipur"),
    Customer(name="Rohit Kumar", email="rohit.kumar@gmail.com", city="Patna"),
    Customer(name="Sneha Reddy", email="sneha.reddy@gmail.com", city="Hyderabad"),
    Customer(name="Arjun Mehta", email="arjun.mehta@gmail.com", city="Ahmedabad"),
    Customer(name="Kavya Nair", email="kavya.nair@gmail.com", city="Kochi"),
    Customer(name="Vikram Joshi", email="vikram.joshi@gmail.com", city="Pune"),
    Customer(name="Ananya Das", email="ananya.das@gmail.com", city="Kolkata")
]

session.add_all(customers)
session.commit()

# Add products
products = [
    Product(name="Dell Inspiron Laptop", category="Electronics", price=62000, stock=10),
    Product(name="iPhone 14", category="Mobile", price=75000, stock=15),
    Product(name="Samsung Smart TV", category="Appliances", price=45000, stock=7),
    Product(name="Boat Bluetooth Speaker", category="Accessories", price=2500, stock=50),
    Product(name="Sony Headphones", category="Accessories", price=4000, stock=30),
    Product(name="HP Wireless Mouse", category="Computer Accessories", price=800, stock=100),
    Product(name="Logitech Keyboard", category="Computer Accessories", price=1500, stock=60),
    Product(name="Mi Power Bank", category="Mobile Accessories", price=1200, stock=80),
    Product(name="Amazon Echo Dot", category="Smart Devices", price=3500, stock=25),
    Product(name="Canon DSLR Camera", category="Electronics", price=55000, stock=5)
]

session.add_all(products)
session.commit()

# Add orders (now IDs exist)
orders = [
    Order(customer_id=customers[0].id, product_id=products[1].id, quantity=1, total_price=75000, order_date=date(2024, 3, 10), status="Delivered"),
    Order(customer_id=customers[1].id, product_id=products[0].id, quantity=1, total_price=62000, order_date=date(2024, 3, 12), status="Shipped"),
    Order(customer_id=customers[2].id, product_id=products[3].id, quantity=2, total_price=5000, order_date=date(2024, 3, 15), status="Pending"),
    Order(customer_id=customers[3].id, product_id=products[4].id, quantity=1, total_price=4000, order_date=date(2024, 3, 18), status="Delivered"),
    Order(customer_id=customers[4].id, product_id=products[2].id, quantity=1, total_price=45000, order_date=date(2024, 3, 20), status="Cancelled"),
    Order(customer_id=customers[5].id, product_id=products[5].id, quantity=3, total_price=2400, order_date=date(2024, 3, 21), status="Delivered"),
    Order(customer_id=customers[6].id, product_id=products[7].id, quantity=2, total_price=2400, order_date=date(2024, 3, 22), status="Pending"),
    Order(customer_id=customers[7].id, product_id=products[8].id, quantity=1, total_price=3500, order_date=date(2024, 3, 23), status="Shipped"),
    Order(customer_id=customers[8].id, product_id=products[6].id, quantity=1, total_price=1500, order_date=date(2024, 3, 24), status="Delivered"),
    Order(customer_id=customers[9].id, product_id=products[9].id, quantity=1, total_price=55000, order_date=date(2024, 3, 25), status="Pending")
]

session.add_all(orders)
session.commit()

print("Data Inserted Successfully")