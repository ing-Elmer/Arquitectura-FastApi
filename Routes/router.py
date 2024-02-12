from fastapi import APIRouter, Depends
from Config.config import SessionLocal
from sqlalchemy.orm import Session
from Models.Users import  RequestUser
from Controller.user_controller import UserController


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
@router.post("/user", tags=["User"])
async def create_user(request: RequestUser, db: Session = Depends(get_db)):
    return await UserController.create_user(request, db)
