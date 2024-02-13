from fastapi_mail import FastMail, ConnectionConfig
from pydantic import BaseModel, EmailStr
from typing import List
# sistema operativo
import os
# variables de entorno
from dotenv import load_dotenv
# dependencias 
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Cargar variables de entorno desde el archivo .env
load_dotenv()

class ConexionBD:
    DB_USERNAME= os.getenv("DB_USERNAME")
    DB_PASSWORD= os.getenv("DB_PASSWORD")
    DB_HOST= os.getenv("DB_HOST")
    DB_NAME= os.getenv("DB_NAME")
    DATABASE_URL = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"
    Engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=Engine)
    Base = declarative_base()
        
    def create_tables(self):
        try:  
            self.Base.metadata.create_all(self.Engine)
            print("Tablas creadas")
        except Exception as e:
            print(f"Error al crear las tablas: {str(e)}")
        
    def drop_tables(self):
        try:
            self.Base.metadata.drop_all(self.Engine)
            print("Tablas eliminadas")
        except Exception as e:
            print(f"Error al eliminar las tablas: {str(e)}")
        
    # Obtener la sesión de la base de datos
    def get_db(self):
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()
    
    def verificar_conexion(self):
        try:
            with self.Engine.connect():
                print("Conexión exitosa")
                return True
        except Exception as e:
            print(f"Error de conexión: {e}")
            return False


load_dotenv()

class EmailManager:
    # Configuración de mail
    conf = ConnectionConfig(
        MAIL_USERNAME=os.getenv("MAIL_USERNAME",""),
        MAIL_PASSWORD=os.getenv("MAIL_PASSWORD",""),
        MAIL_FROM=os.getenv("MAIL_FROM",""),
        MAIL_PORT=587,
        MAIL_SERVER="smtp.gmail.com",
        MAIL_STARTTLS=True,
        MAIL_SSL_TLS=False,
        VALIDATE_CERTS = True
    )