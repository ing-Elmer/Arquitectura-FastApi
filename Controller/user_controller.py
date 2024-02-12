from Models.Users import RequestUser, ResponseUser
from Mails.send_email import send_mail
from fastapi import Depends, HTTPException
from Config.config import get_db
from sqlalchemy.orm import Session
from Service.user_service import UserService

class UserController:
    
    async def create_user(request: RequestUser, db: Session = Depends(get_db)):
        try:
            email_address = request.parameter.email
            # Llama al método send_mail con la dirección de correo electrónico
            await send_mail(email_address)
            user_created = UserService().create_user(db, user=request.parameter)
        except Exception as e:
            # Maneja el fallo del envío de correo electrónico
            raise HTTPException(status_code=500, detail=f"No se pudo enviar el correo electrónico: {str(e)}")

        # Retorna la respuesta al cliente
        return ResponseUser(code=200, status="success", message="Usuario registrado correctamente", result=user_created).dict(exclude_none=True)
