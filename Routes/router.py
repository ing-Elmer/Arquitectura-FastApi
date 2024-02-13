from fastapi import APIRouter, Depends
from Config.config import ConexionBD
from sqlalchemy.orm import Session
from Models.Users import  RequestUser
from Controller.user_controller import UserController


router = APIRouter()
    
@router.post("/user", tags=["User"])
async def create_user(request: RequestUser, db: Session = Depends(ConexionBD().get_db)):
    return await UserController.create_user(request, db)
