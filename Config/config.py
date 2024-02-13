from fastapi_mail import FastMail, ConnectionConfig
from pydantic import BaseModel, EmailStr
from typing import List
# sistema operativo
import os
# variables de entorno
from dotenv import load_dotenv

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