from Api.Models.Users import RequestUser, ResponseUser, RequestUserLogin
from Core.Emails.email import EmailManager
from fastapi import Depends, HTTPException
from Api.Data.connection_data import ConexionBD
from sqlalchemy.orm import Session
from Api.Service.user_service import UserService
class UserController:
    
    async def create_user(request: RequestUser, db: Session = Depends(ConexionBD().get_db)):

        email= request.parameter.email
        name = request.parameter.name
        otp = "1da-sd22DA-SDAD-A3DASDA-4"
        link = f"http://localhost:5173/{otp}"
        # Llama al método send_mail con la dirección de correo electrónico
        await EmailManager().send_email(email, "Registro de Usuario", name, link)
        user_created = UserService().create_user(db, user=request.parameter)
        # Retorna la respuesta al cliente
        return ResponseUser(code=200, status="success", message="Usuario registrado correctamente", result=user_created).model_dump(exclude_none=True)

    def login(request: RequestUserLogin, db: Session = Depends(ConexionBD().get_db)):
        try:
            return UserService().login_user(db, request.parameter.email, request.parameter.password)
        except ValueError as e:
            raise HTTPException(status_code=401, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))