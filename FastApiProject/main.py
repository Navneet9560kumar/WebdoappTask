#fast api app

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

import models
import crud
import schemas
from database import engine, get_db

# Tables auto-create ho jaen gi MySQL mein
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI MySQL CRUD", version="1.0.0")


# ─── CREATE ────────────────────────────────────────────────────────────────────
@app.post("/users/", response_model=schemas.UserResponse, status_code=201)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing = crud.get_user_by_email(db, email=user.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


# ─── READ ALL ──────────────────────────────────────────────────────────────────
@app.get("/users/", response_model=List[schemas.UserResponse])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_users(db, skip=skip, limit=limit)


# ─── READ ONE ──────────────────────────────────────────────────────────────────
@app.get("/users/{user_id}", response_model=schemas.UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


# ─── UPDATE ────────────────────────────────────────────────────────────────────
@app.put("/users/{user_id}", response_model=schemas.UserResponse)
def update_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    db_user = crud.update_user(db, user_id=user_id, user=user)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


# ─── DELETE ────────────────────────────────────────────────────────────────────
@app.delete("/users/{user_id}", response_model=schemas.UserResponse)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.delete_user(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


# ─── HEALTH CHECK ──────────────────────────────────────────────────────────────
@app.get("/")
def root():
    return {"message": "API chal rahi hai bhai!"}