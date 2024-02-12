from fastapi import HTTPException
from fastapi.responses import JSONResponse
from fastapi_mail import FastMail, MessageSchema, MessageType
from Config.config import conf, EmailSchema

async def send_mail(email: EmailSchema) -> JSONResponse:
    # Cargar el contenido HTML desde el archivo
    with open("Utils/Templates/Email.html", "r") as file:
        html_content = file.read()

    # Adjuntar la imagen del logo
    adjunto = {
        "file": "Utils/Image/logo-2.png",
        "filename": "logo.png",
        "type": "image/png",
        "headers": {"Content-ID": "<logo>"}
    }

    # Configurar el mensaje de correo electrónico
    contenido_correo = MessageSchema(
        subject="Activación de cuenta",
        recipients=[email.email],  # Acceder al atributo email de EmailSchema
        body=html_content,
        subtype=MessageType.html,
        attachments=[adjunto],
    )

    # Inicializar FastMail
    fm = FastMail(conf)

    try:
        # Enviar el correo electrónico
        await fm.send_message(contenido_correo)
    except Exception as e:
        # Manejar excepciones (por ejemplo, problemas de red, errores de autenticación)
        raise HTTPException(status_code=500, detail=f"No se pudo enviar el correo electrónico: {e}")

    # Éxito. El correo electrónico se envió correctamente
    return JSONResponse(content={"message": "Correo electrónico enviado correctamente"}, status_code=200)
