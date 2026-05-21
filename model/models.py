from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    products = relationship("Product", back_populates="category")


class Manufacturer(Base):
    __Tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)

    products = relationship("Product", back_populates="manufacturer")


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    prince = Column(Float)
    quantity = Column(Integer)
    category_id = Column(Integer, ForeignKey("categories.id"))
    manufacturer_id = Column(Integer, ForeignKey("manufacturers.id"))

    category = relationship("Category", back_populates="products")
    manufacturer = relationship("Manufacturer", back_populates="products")



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    cart = relationship("Cart", back_populates="user")


class Cart(Base):
    __tablename__ = "carts"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="cart")
    items = relationship("CartItems", back_populates="cart")


class CartItems(Base):
    __tablename__ = "cart_items"

    id = Column(Integer, primary_key=True)
    cart_id = Column(Integer, ForeignKey("carts.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)

    cart = relationship("Cart", back_populates="items")
    product = relationship("Product")