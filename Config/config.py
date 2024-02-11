from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi_mail import FastMail, ConnectionConfig
from pydantic import BaseModel, EmailStr
from typing import List


DATABASE_URL = "postgresql://postgres:admin@localhost:5432/prueba"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
class EmailSchema(BaseModel):
    email: List[EmailStr]
    

conf = ConnectionConfig(
    MAIL_USERNAME="practicaprograuniversidad@gmail.com",
    MAIL_PASSWORD="igjg nqqq iidr xqge",
    MAIL_FROM="practicaprograuniversidad@gmail.com",
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False
)