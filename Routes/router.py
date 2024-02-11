from fastapi import APIRouter, HTTPException, Path, Depends
from Config.config import SessionLocal
from sqlalchemy.orm import Session
from Models.Users import UserSchema, RequestUser, ResponseUser
from Service import UserService
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


@router.get("/user", tags=["User"])
async def get_users(db: Session = Depends(get_db)):
    _users = UserService.get_user(db, 0, 100)
    return ResponseUser(code=200, status="success", message="Usuarios", result=_users).dict(exclude_none=True)

@router.get("/user/{id}", tags=["User"])
async def get_user_by_id(id: int, db: Session = Depends(get_db)):
    _user = UserService.get_user_by_id(db, id)
    if _user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return ResponseUser(code=200, status="success", message="Usuario", result=_user).dict(exclude_none=True)

@router.put("/user/{id}", tags=["User"])
async def update_user(id: int, request: RequestUser, db: Session = Depends(get_db)):
    _user = UserService.update_user(db, user_id=request.parameter.id, name = request.parameter.name, last_name = request.parameter.last_name, email = request.parameter.email, password = request.parameter.password)
    return ResponseUser(code=200, status="success", message="Usuario actualizado correctamente", result=_user)

@router.delete("/user/{id}", tags=["User"])
async def delete_user(id: int, db: Session = Depends(get_db)):
    UserService.remove_user(db, user_id=id)
    return ResponseUser(code=200, status="success", message="Usuario eliminado correctamente", result=None)