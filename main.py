from fastapi import FastAPI, Depends, HTTPException
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

@app.get("/addresses", response_model=list[schemas.AddressOut])
def get_all_addresses(db: Session = Depends(get_db)):
    return crud.get_addresses(db)

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
