from app.db.session import engine, SessionLocal
from app.db.base import Base
from app.models.user import User

# create table
Base.metadata.create_all(bind=engine)

#Create DB sessions
db = SessionLocal()


# Insert data
new_user = User(
    name="Navneet",
    email="navneet@gmail.com"
)

db.add(new_user)

db.commit()

print("User inserted successfully 🚀")