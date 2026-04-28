# CRUD = Create, Read, Update, Delete
# Ye file sirf DB se baat karti hai
# Main.py routes yahan se functions call karte hain

from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas import UserCreate, UserUpdate

# Ek user ID se dhundo
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

# Email se dhundo (duplicate check ke liye)
def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

# Saare users laao
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

# Naya user banao
def create_user(db: Session, user: UserCreate):
    db_user = User(
        name=user.name,
        email=user.email,
        phone=user.phone
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# User update karo
def update_user(db: Session, user_id: int, user: UserUpdate):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        return None
    update_data = user.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user

# User delete karo
def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        return None
    db.delete(db_user)
    db.commit()
    return db_user