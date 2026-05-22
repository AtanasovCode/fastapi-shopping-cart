from sqlalchemy.orm import Session
from model.models import Product
from model.schemas import ProductCreate, ProductUpdate


def list_all(db: Session):
    return db.query(Product).all()


def find_by_id(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()


def save(db: Session, product_create: ProductCreate):
    new_product = Product(**product_create.model_dump())

    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


def update(db: Session, product_update: ProductUpdate, product_id: int):
    target = find_by_id(db, product_id)

    if not target:
        return None

    for key, value in product_update.model_dump(exclude_unset=True).items():
        setattr(target, key, value)

    db.commit()
    db.refresh(target)
    return target


def delete(db: Session, product_id: int):
    target = find_by_id(db, product_id)

    if not target:
        return None
    
    db.delete(target)
    db.commit()
    return target