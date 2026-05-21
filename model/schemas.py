from pydantic import BaseModel
from typing import Optional


class CategorySchema(BaseModel):
    id: int
    name: str
    description: str


class ManufacturerSchema(BaseModel):
    id: int
    name: str
    address: str


class ProductSchema(BaseModel):
    id: int
    name: str
    price: float
    quantity: int
    category: CategorySchema
    manufacturer: ManufacturerSchema


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None
    category_id: Optional[int] = None
    manufacturer_id: Optional[int] = None


class ProductCreate(BaseModel):
    name: str
    price: float
    quantity: int
    category_id: int
    manufacturer_id: int