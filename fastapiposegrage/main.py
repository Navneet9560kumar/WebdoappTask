from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

import Models
import crud
import Schemas
from Database import engine, get_db

#Table auto-create hongi postgres
Models.Base.metadata.create_all(bind=engine)

app= FastAPI(title="FastAPI PostgreSQL crud", version="1.0.0")

@app.on_event("startup")
async def startup():
    print("✅ Database Connected Successfully!")

#create
 
@app.post("/users/",response_model=Schemas.UserResponse, status_code=201)
def create_user(user:Schemas.UserCreate, db: Session=  Depends(get_db)):
      existing = crud.get_user_by_email(db=db, email=user.email)
      if existing:
            raise HTTPException(status_code=400, detail="Email already registered")
      return crud.create_user(db=db, user=user)

#READ one
@app.get("/users/{user_id}", response_model=Schemas.UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
      db_user = crud.get_user(db, user_id=user_id)
      if not db_user:
            raise HTTPException(status_code=404, detail="User not found")
      return db_user

#UPDATE 
@app.put("/users/{user_id}",response_model = Schemas.UserResponse)
def update_user(user_id:int, user: Schemas.UserUpdate, db:Session=Depends(get_db)):
      db_user = crud.update_user(db, user_id=user_id, user= user)
      if not db_user:
            raise HTTPException(status_code=404, detail="User not found")
      return db_user

#DELETE 
@app.delete("/users/{user_id}",response_model=Schemas.UserResponse)
def delete_user(user_id: int, db: Session = Depends(get_db)):
      db_user = crud.delete_user(db, user_id=user_id)
      if not db_user:
            raise HTTPException(status_code=404, detail="User not found")
      return db_user

#Get all users with count
@app.get("/users-count/")
def get_users_count(db: Session = Depends(get_db)):
      total_users = crud.get_users(db)
      return {
            "total_users": len(total_users),
            "users": total_users
      }

#Health check
@app.get("/")
def root():
    return {"message": "API chal rahi hai bhai!"}           
