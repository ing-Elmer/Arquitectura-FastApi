from Api.Models.Users import RequestUser, ResponseUser, RequestUserLogin,RequestUserUpdate, ResponseUserUpdate
from Core.Emails.email import EmailManager
from fastapi import Depends, HTTPException
from Api.Data.connection_data import ConexionBD
from sqlalchemy.orm import Session
from Api.Service.user_service import UserService
from Core.Validators.error import CustomError


class UserController:
    
    async def create_user(request: RequestUser, db: Session = Depends(ConexionBD().get_db)):
        try: 
            email= request.parameter.email
            name = request.parameter.name
            otp = "1da-sd22DA-SDAD-A3DASDA-4"
            link = f"http://localhost:5173/{otp}"
            # Llama al método send_mail con la dirección de correo electrónico
            await EmailManager().send_email(email, "Registro de Usuario", name, link)
            user_created = UserService().create_user(db, user=request.parameter)
            # Retorna la respuesta al cliente
            return ResponseUser(code=200, status="success", message="Usuario registrado correctamente", result=user_created).model_dump(exclude_none=True)
        except CustomError as e:
            raise e
        except ValueError as e:
            raise HTTPException(status_code=401, detail=str(e))
        except Exception as e:
            raise CustomError(500, f"Error en el servidor, por favor vuelva a intentar mas tarde: {str(e)}")
        
    def login(request: RequestUserLogin, db: Session = Depends(ConexionBD().get_db)):
        try:
            return UserService().login_user(db, request.parameter.email, request.parameter.password)
        except CustomError as e:
            raise e
        except ValueError as e:
            raise HTTPException(status_code=401, detail=str(e))
        except Exception as e:
            raise CustomError(500, f"Error en el servidor, por favor vuelva a intentar mas tarde: {str(e)}")
        
    def get_user_by_id(user_id: int, db: Session = Depends(ConexionBD().get_db)):
        try:
            user = UserService().get_user_by_id(db, user_id)
            return ResponseUser(code=200, status="success", message="Usuario obtenido correctamente", result=user).model_dump(exclude_none=True)
        except CustomError as e:
            raise e
        except ValueError as e:
            raise HTTPException(status_code=401, detail=str(e))
        #excepcion de permisos
        except HTTPException as e:
            if e.status_code == 403:
                raise CustomError(403, f"No tienes permisos para realizar la acción: {str(e)}")
            elif e.status_code == 401:
                raise CustomError(401, f"El usuario debe estar autentificado: {str(e)}")
            elif e.status_code == 404:
                raise CustomError(404, f"Usuario no encontrado: {str(e)}")
            elif e.status_code == 400:
                raise CustomError(400, f"Error en la petición: {str(e)}")

        except Exception as e:
            raise CustomError(500, f"Ocurrio un error inesperado, por favor vuelva a intentar mas tarde: {str(e)}")

    @staticmethod
    def get_user(db: Session = Depends(ConexionBD().get_db), skipt: int = 0, limit: int = 100):
        try:
            users = UserService().get_user(db, skipt, limit)
            return ResponseUser(code=200, status="success", message="Usuarios obtenidos correctamente", result=users).model_dump(exclude_none=True)
        except CustomError as e:
            raise e
        except HTTPException as e:
            if e.status_code == 403:
                raise CustomError(403, f"Error de permisos: {str(e)}")
            elif e.status_code == 401:
                raise CustomError(401, f"Error al autenticarse: {str(e)}")
        except Exception as e:
            raise CustomError(500, f"Error en el servidor, por favor vuelva a intentar mas tarde: {str(e)}")
        
    def update_user(user_id: int, request: RequestUserUpdate, db: Session = Depends(ConexionBD().get_db)):
        try:
            user = UserService().update_user(db, user_id, request.parameter)
            return ResponseUserUpdate(code=200, status="success", message="Usuario actualizado correctamente", result=user).model_dump(exclude_none=True)
        except CustomError as e:
            raise e
        except ValueError as e:
            raise HTTPException(status_code=401, detail=str(e))
        except Exception as e:
            raise CustomError(500, f"Error en el servidor, por favor vuelva a intentar mas tarde: {str(e)}")
