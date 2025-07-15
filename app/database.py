from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Connection URL format:
# postgresql://username:password@hostname:port/database_name
DATABASE_URL = "postgresql://postgres:Tsehaye7@localhost:5432/books_db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
