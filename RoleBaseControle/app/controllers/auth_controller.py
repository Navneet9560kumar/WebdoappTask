# Login aur Register ka logic


from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.user import User
from app.schemas.user_schema import UserRegister
from app.middlewares.auth import hash_password, verify_password, create_access_token

def register_user(data: UserRegister, db: Session):
      """ Naya userr register karega """



 

 
