from sqlalchemy.orm import Session
from Models.Users import UserSchema
from Data.data import User
from passlib.hash import bcrypt
import os

# Obtener todos los usuarios
def get_user(db: Session, skipt: int = 0, limit: int = 100):
    return db.query(User).offset(skipt).limit(limit).all()

# Obtener un usuario por su id
def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

#Generar un salto seguro
def generate_salt(length=32):
    return os.urandom(length).hex()

#Hashear una contraseña usando bcrypt:
def hash_password(password, salt):
    return bcrypt.hash(password, salt=salt)

#Verificar una contraseña comparando el hash:
def verify_password(password, hashed_password):
    return bcrypt.verify(password, hashed_password)

# Crear un usuario
def create_user(db: Session, user: UserSchema):
    # Generar la sal y hashear la contraseña
    salt = generate_salt()
    hashed_password = hash_password(user.password, salt)

    _user = User(
        name=user.name,
        last_name=user.last_name,
        email=user.email,
        password=hashed_password,
        salt=salt
    )
    db.add(_user)
    db.commit()
    db.refresh(_user)
    return _user

# Eliminar un usuario
def remove_User(db: Session, user_id: int):
    _user = get_user_by_id(db=db, user_id=user_id)
    db.delete(_user)
    db.commit()

# Actualizar un usuario
def update_user(db: Session, user_id: int, user: UserSchema):
    _user = get_user_by_id(db=db, user_id=user_id)
    _user.name = user.name
    _user.last_name = user.last_name
    _user.email = user.email
    _user.password = user.password
    db.commit()
    db.refresh(_user)
    return _user
