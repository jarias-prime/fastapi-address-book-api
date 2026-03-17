from fastapi import FastAPI, Depends, HTTPException

from database import SessionLocal, engine, Base

app = FastAPI(title="Address Book API")

# Create database tables
Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    
    try:
        yield db
    finally:
        db.close()