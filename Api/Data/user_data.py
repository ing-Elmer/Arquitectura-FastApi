from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, Text, text
from Api.Data.connection_data import ConexionBD

class User(ConexionBD.Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=255), index=True)
    last_name = Column(String(length=255), index=True)
    email = Column(String(length=255), unique=True, index=True)
    password = Column(String(length=255))
    phone = Column(Integer, index=True)
    image = Column(Text, nullable=True)
    otp = Column(String(length=255), nullable=True)
    role = Column(String(length=20), default='user')
    birthdate = Column(TIMESTAMP, nullable=True)
    is_active = Column(Boolean, default=True)
    term_conditions = Column(Boolean, default=False)
    is_verified = Column(Boolean, default=False)
    last_login = Column(TIMESTAMP, nullable=True)
    date_joined = Column(TIMESTAMP, server_default=text('now()'))
    created_at = Column(TIMESTAMP, server_default=text('now()'))
    updated_at = Column(TIMESTAMP, server_default=text('now()'), onupdate=text('now()'))
