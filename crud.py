from sqlalchemy.orm import Session
import models

def create_address(db: Session, address):
    db_address = models.Address(**address.dict())
    db.add(db_address)
    db.commit()
    db.refresh(db_address)

    return db_address

def get_addresses(db: Session, page: int = 1, page_size: int = 10):
    offset = (page - 1) * page_size

    return db.query(models.Address).offset(offset).limit(page_size).all()

def update_address(db: Session, address_id: int, updated_data):
    address = db.query(models.Address).filter(models.Address.id == address_id).first()

    if not address:
        return None
    for key, value in updated_data.dict().items():
        setattr(address, key, value)
   
    db.commit()
    db.refresh(address)

    return address

def delete_address(db: Session, address_id: int):
    address = db.query(models.Address).filter(models.Address.id == address_id).first()
    
    if not address:
        return None

    db.delete(address)
    db.commit()

    return address