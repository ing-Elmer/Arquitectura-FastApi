
from fastapi_mail import FastMail, MessageSchema, MessageType
from fastapi.responses import JSONResponse
from fastapi_mail import FastMail
from Config.config import conf, EmailSchema


async def send_mail(email: EmailSchema) -> JSONResponse:
    # Cargar el contenido HTML desde el archivo
    with open("Utils/Templates/Email.html", "r") as file:
        html_content = file.read()

    adjunto ={
        "file": "Utils/Image/logo-2.png",
        "filename": "logo.png",
        "type": "image/png",
        "headers": {
            "Content-ID": "<logo>"
        }
    }
    # Configurar el mensaje con el contenido HTML
    email_content = MessageSchema(
        subject="Activación de cuenta",
        recipients=[email],
        body=html_content,
        subtype=MessageType.html,
        attachments=[adjunto],
    )

    # Enviar el mensaje
    fm = FastMail(conf)
    await fm.send_message(email_content)