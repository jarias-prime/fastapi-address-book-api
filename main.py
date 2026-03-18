from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
import math

import models, schemas, crud
from database import SessionLocal, engine, Base

app = FastAPI(
    title="Address Book API", 
    docs_url="/",
    redoc_url=None
)

# Create database tables
Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

@app.post("/addresses", response_model=schemas.AddressOut)
def create_address(address: schemas.AddressCreate, db: Session = Depends(get_db)):
    return crud.create_address(db, address)

@app.get("/addresses")
def get_all_addresses(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db)
):
    data = crud.get_addresses(db, page, page_size)
    total = db.query(models.Address).count()

    total_pages = (total + page_size - 1) // page_size

    return {
        "page": page,
        "page_size": page_size,
        "total": total,
        "total_pages": total_pages,
        "data": data
    }

@app.put("/addresses/{address_id}", response_model=schemas.AddressOut)
def update_address(address_id: int, updated: schemas.AddressUpdate, db: Session = Depends(get_db)):
    address = crud.update_address(db, address_id, updated)

    if not address:
        raise HTTPException(status_code=404, detail="Address not found")

    return address

@app.delete("/addresses/{address_id}")
def delete_address(address_id: int, db: Session = Depends(get_db)):
    address = crud.delete_address(db, address_id)

    if not address:
        raise HTTPException(status_code=404, detail="Address not found")

    return {"message": "Deleted successfully"}
