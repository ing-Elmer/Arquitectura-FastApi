from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field

T = TypeVar('T')

class UserSchema(BaseModel):
    id: Optional[int] = None
    name: str
    last_name: str
    email: str
    password: str
    is_active: Optional[bool] = True
    phone: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    class Config:
        from_attributes = True

class RequestUser(BaseModel):
    parameter: UserSchema = Field(...)

class ResponseUser(BaseModel, Generic[T]):
    code: int
    status: str
    message: str
    result: Optional[T]