# is file mai humne apna base class banaya hai jisme sqlalchemy ka declarative base use kiya hai taki hum apne models ko is base class se inherit kar sake aur database ke sath interact kar sake

from sqlalchemy.orm import declarative_base

Base = declarative_base()