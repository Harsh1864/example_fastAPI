import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor


# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:Harsh6567@localhost/fastAPI'
DATABASE_URL = os.getenv('DATABASE_URL')
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

engine = create_engine(DATABASE_URL)
# engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()


# #for connect the database
# try:
#     conn = psycopg2.connect(host='localhost',database='fastAPI',user='postgres',password='Harsh6567',cursor_factory=RealDictCursor)
#     cursor = conn.cursor()
#     print("Database was connecting sucessfully")
# except Exception as error:
#     print("Database connection was failed")
#     print("Error:",error)
