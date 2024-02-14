from fastapi import APIRouter, Depends
from Api.Data.connection_data import ConexionBD
from sqlalchemy.orm import Session
from Api.Models.Users import  RequestUser, RequestUserLogin, ResponseUser, UserModel, RequestUserUpdate
from Api.Controller.user_controller import UserController


router = APIRouter()
    
@router.post("/", tags=["User"])
async def create_user(request: RequestUser, db: Session = Depends(ConexionBD().get_db)):
    return await UserController.create_user(request, db)

@router.post("/login", tags=["User"])
async def login(request: RequestUserLogin, db: Session = Depends(ConexionBD().get_db)):
    return UserController.login(request, db)

@router.get("/{user_id}", tags=["User"])
async def get_user_by_id(user_id: int, db: Session = Depends(ConexionBD().get_db)):
    return UserController.get_user_by_id(user_id, db)

@router.get("/", tags=["User"])
async def get_user(db: Session = Depends(ConexionBD().get_db), skipt: int = 0, limit: int = 100):
    return UserController.get_user(db, skipt, limit)

@router.put("/{user_id}", tags=["User"])
async def update_user(user_id: int, request: RequestUserUpdate, db: Session = Depends(ConexionBD().get_db)):
    return UserController.update_user(user_id, request, db)