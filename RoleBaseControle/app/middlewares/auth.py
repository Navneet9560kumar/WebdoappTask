#app/middlewares/auth.py
#jwt token banane aur verify karne ka logic yaha hai 
#Har protected route mein ye use hoga

from datetime import datetime,timedelta,timezone
from jose import JWTError,jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
import os
from dotenv import load_dotenv

from app.db.session import get_db
from app.models.user import User

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY","changame")
ALGORITHM = os.getenv("ALGORITHM","HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

# Password hashing
pwd_context = CryptContext(schemes =["bcrypt"],deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def hash_password(password:str)->str:
      """ ab yaha plain password ko hash karenge"""
      return pwd_context.hash(password)

def verify_password(plain:str,hashed:str)->bool:
      """ yaha pe plain passwrd ko hashed password se compare karenge"""
      return pwd_context.verify(plain,hashed)

def create_access_token(data:dict,expires_delta:timedelta=None)->str:
      """ yaha per jwt ka logic genrate karenge or token ke expres hone ka wait karge """
      to_encode = data.copy()
      expire = datetime.now(timezone.utc)+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
      to_encode.update({"exp":expire})
      return jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)


def get_current_user(token:str=Depends(oauth2_scheme),
                     db:Session= Depends(get_db)
                   )-> User:
      """ Token se current logged-in user nikalo"""
      credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers = {"WWW-Authenticate":"Bearer"},
      )
      try:
            payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
            user_id:int= payload.get("sub")
            if user_id is None:
                  raise credentials_exception
      except JWTError:
            raise credentials_exception
      
      user = db.query(User).filter(User.id == int(user_id),User.is_active == True).first()
      if not user:
            raise credentials_exception
      return user