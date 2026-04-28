from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db_url = "postgresql://postgres:9560Navneet@localhost:5432/mydatabase"

engine = create_engine(db_url)

# Connection check karne ke liye logic
try:
    with engine.connect() as connection:
        print("✅ Database connection successful!")
except Exception as e:
    print(f"❌ Database connection failed: {e}")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()