#ye mere file MySQL connection ka code hai

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv()

# .env file mein ye variables set kar:
# DB_USER=root
# DB_PASSWORD=yourpassword
# DB_HOST=localhost
# DB_PORT=3306
# DB_NAME=mydb

DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME", "mydb")

# URL-encode the password to handle special characters like @
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{quote_plus(DB_PASSWORD)}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Test database connection
try:
    with engine.connect() as connection:
        print("✅ Database connected successfully!")
except Exception as e:
    print(f"❌ Database connection failed: {e}")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()