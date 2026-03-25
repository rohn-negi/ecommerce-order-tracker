from sqlalchemy import create_engine, String, Float, Integer, ForeignKey, Column, Date
from sqlalchemy.orm import declarative_base, Session, relationship
from sqlalchemy import CheckConstraint

engine = create_engine("mysql+mysqlconnector://root:@localhost/school", echo=False)
Base = declarative_base()

class Customer(Base):
    __tablename__ = "customers_ecom"

    id    = Column(Integer, primary_key=True, autoincrement=True)
    name  = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    city  = Column(String(100), nullable=False)

    orders = relationship("Order", back_populates="customer")


class Product(Base):
    __tablename__ = "products_ecom"

    id       = Column(Integer, primary_key=True, autoincrement=True)
    name     = Column(String(150), nullable=False)
    category = Column(String(150))
    price    = Column(Float, nullable=False)
    stock    = Column(Integer)

    __table_args__ = (
        CheckConstraint("price > 0", name="check_price"),
    )

    orders = relationship("Order", back_populates="product")


class Order(Base):
    __tablename__ = "orders_ecom"

    id          = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers_ecom.id"), nullable=False)
    product_id  = Column(Integer, ForeignKey("products_ecom.id"), nullable=False)
    quantity    = Column(Integer, nullable=False)
    total_price = Column(Float, nullable=False)
    order_date  = Column(Date, nullable=False)
    status      = Column(String(20), default="Pending")

    __table_args__ = (
        CheckConstraint("quantity > 0", name="check_quantity"),
        CheckConstraint("total_price > 0", name="check_total_price"),
    )

    customer = relationship("Customer", back_populates="orders")
    product  = relationship("Product", back_populates="orders")


Base.metadata.create_all(engine)
print("All tables created.")

