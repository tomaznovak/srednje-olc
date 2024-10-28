from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg
import time
from .config import settings

SQLALCHEMY_DATABASE_URL = f'postgresql+psycopg://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



# code for connecting raw to sql database
# while True:
#     try:
#         conn = psycopg.connect("dbname=fastapi user=postgres password=pepsicola1.")
#         cursor = conn.cursor()
#         print('Database connection was succesfull!')
#         break

#     except Exception as e:
#         print("Connecting to database failed")
#         print(f'Error was {e}')
#         time.sleep(2)
