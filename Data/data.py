from sqlalchemy import String,Boolean, Column, Integer, text, TIMESTAMP
from Config.config import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    phone = Column(Integer, index=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP, server_default=text('now()'))
    updated_at = Column(TIMESTAMP, server_default=text('now()'), onupdate=text('now()'))