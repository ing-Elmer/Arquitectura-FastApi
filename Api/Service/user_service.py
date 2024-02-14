from sqlalchemy.orm import Session
from Api.Models.Users import UserModel
from Api.Data.user_data import User
from Core.Security.security_encryption import SecurityEncryption
from Core.Security.security_auth import JWT
from Core.Validators.validator_models import ValidatorModels
from Core.Validators.error import CustomError

class UserService:
    
    # Obtener todos los usuarios
    @staticmethod
    def get_user(db: Session, skipt: int = 0, limit: int = 100):
        return db.query(User).offset(skipt).limit(limit).all()

    # Obtener un usuario por su id
    @staticmethod
    def get_user_by_id(db: Session, user_id: int):
        return db.query(User).filter(User.id == user_id).first()

    # Crear un usuario
    @staticmethod
    def create_user( db: Session, user: UserModel):
        # Hashea la contraseña antes de almacenarla
        token = JWT().create_access_token({"sub": user.name},token_type="activate", expires_minutes=60)
        hashed_password = SecurityEncryption.hash_password(user.password)
        _user = User(
            name=user.name,
            last_name=user.last_name,
            email=user.email,
            password=hashed_password,
            phone=user.phone,
            otp=token,
        )
        db.add(_user)
        db.commit()
        db.refresh(_user)
        return _user
    
    # Eliminar un usuario
    @staticmethod
    def remove_User(self,db: Session, user_id: int):
        _user = self.get_user_by_id(db=db, user_id=user_id)
        db.delete(_user)
        db.commit()

    # Actualizar un usuario
    @staticmethod
    def update_user(self, db: Session, user_id: int, user: UserModel):
        _user = self.get_user_by_id(db=db, user_id=user_id)

        # Verifica si el usuario que realiza la actualización es el dueño de la cuenta
        if _user.id != user_id:
            raise CustomError(403, "No tienes permisos para actualizar este usuario.")

        # Resto del código para la actualización del usuario
        hashed_password = SecurityEncryption.hash_password(user.password)
        _user.name = user.name
        _user.last_name = user.last_name
        _user.email = user.email
        _user.password = hashed_password

        db.commit()
        db.refresh(_user)
        return _user
    
    # Método para el inicio de sesión
    @staticmethod
    def login_user( db: Session, email: str, password: str):
        user = db.query(User).filter(User.email == email).first()
        ValidatorModels.validate_user_exists(user)
        ValidatorModels.validate_user_verified(user.is_verified)
        ValidatorModels.validate_user_active(user.is_active)
        ValidatorModels.validate_credentials(password, user.password)  
        
        # Si todas las validaciones pasan, crea un token de acceso
        token = JWT().create_access_token({"sub": user.id},token_type="access", expires_minutes=60)
        return {"user": user,"access": token, "token_type": "bearer"}



