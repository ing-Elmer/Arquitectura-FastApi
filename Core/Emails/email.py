
# sistema operativo
import os
from email_validator import validate_email, EmailNotValidError
from fastapi_mail import FastMail, MessageSchema, MessageType, ConnectionConfig
from Core.Validators.error import CustomError
from jinja2 import Environment, FileSystemLoader
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

    async def send_email(self,to: str, subject: str, name: str, link: str = "http://localhost:5173"):
        try:
            # validar el correo
            valid_email = validate_email(to)
            to = valid_email.email

            # Renderizar el template HTML
            env = Environment(loader=FileSystemLoader("Resources/Templates"))
            template = env.get_template("Email.html")
            html_content = template.render(
                subject=subject, name=name, link=link
            )

            # Obtener la ruta del script actual
            current_path = os.path.dirname(os.path.abspath(__file__))

            # Construir la ruta al archivo de la imagen del logo
            logo_path = os.path.join(current_path, "..", "..", "Resources", "Image", "logo.png")

            # Validar que el archivo exista
            if not os.path.exists(logo_path):
                raise CustomError(500, "El archivo del logo no existe")

            # Crear el adjunto
            adjunto = {
                "file": logo_path,
                "filename": "logo.png",
                "type": "image/png",
                "headers": {
                    "Content-ID": "<logo_image>",
                },
            }

            # Crear el mensaje
            email_content = MessageSchema(
                subject=subject,
                recipients=[to],
                body=html_content,
                subtype=MessageType.html,
                attachments=[adjunto],
            )

            # Enviar el mensaje
            fm = FastMail(self.conf)
            await fm.send_message(email_content)

        except CustomError as e:
            raise e
        
        except EmailNotValidError as e:
            raise CustomError(400, f"El correo {to} no es válido")
        except Exception as e:
            raise CustomError(500, f"Error al enviar el correo: {str(e)}")

