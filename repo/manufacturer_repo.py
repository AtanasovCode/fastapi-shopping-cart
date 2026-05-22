from sqlalchemy.orm import Session
from model.models import Manufacturer

def list_all(db: Session):
    return db.query(Manufacturer).all()

