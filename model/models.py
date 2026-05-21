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