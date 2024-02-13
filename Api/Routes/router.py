from fastapi import APIRouter, Depends
from Api.Data.connection_data import ConexionBD
from sqlalchemy.orm import Session
from Api.Models.Users import  RequestUser, RequestUserLogin
from Api.Controller.user_controller import UserController


router = APIRouter()
    
@router.post("/user", tags=["User"])
async def create_user(request: RequestUser, db: Session = Depends(ConexionBD().get_db)):
    return await UserController.create_user(request, db)

@router.post("/login", tags=["User"])
async def login(request: RequestUserLogin, db: Session = Depends(ConexionBD().get_db)):
    return UserController.login(request, db)
