from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
class JWT:
    def __init__(self):
        self.SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
        self.ALGORITHM = "HS256"
        self.DEFAULT_EXPIRE_MINUTES = 30

    def create_access_token(self, data: dict, expires_minutes: int | None = None):
        to_encode = data.copy()
        expire_minutes = expires_minutes or self.DEFAULT_EXPIRE_MINUTES
        expire = datetime.now(timezone.utc) + timedelta(minutes=expire_minutes)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)
        return encoded_jwt

    def verify_token(self, token: str):
        try:
            payload = jwt.decode(token, self.SECRET_KEY, algorithms=[self.ALGORITHM])
            return payload
        except JWTError:
            return None
        