from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from typing import List, Optional

T = TypeVar('T')

class UserModel(BaseModel):
    id: Optional[int] = None
    name: str
    last_name: str
    email: str
    password: str
    image: Optional[str] = None
    birthdate: Optional[str] = None
    role: Optional[str] = "user"
    term_conditions: Optional[bool] = False
    is_verified: Optional[bool] = False 
    last_login: Optional[str] = None
    is_active: Optional[bool] = True
    phone: Optional[int] = None
    otp: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    class Config:
        from_attributes = True
        
class RequestUser(BaseModel):
    parameter: UserModel = Field(...)
    

class ResponseUser(BaseModel):
    code: int
    status: str
    message: str
    result: Optional[UserModel] = None 
        
class UserUpdateModel(BaseModel):
    name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    image: Optional[str] = None
    birthdate: Optional[str] = None
    phone: Optional[int] = None

    class Config:
        from_attributes = True

class RequestUserUpdate(BaseModel):
    parameter: UserUpdateModel = Field(...)

class ResponseUserUpdate(BaseModel, Generic[T]):
    code: int
    status: str
    message: str
    result: Optional[UserUpdateModel] = None 
    

    

    
class LoginModel(BaseModel):
    email: str
    password: str

class RequestUserLogin(BaseModel):
    parameter: LoginModel
