from passlib.context import CryptContext
class SecurityEncryption:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @staticmethod
    def hash_password(password: str) -> str:
        return SecurityEncryption.pwd_context.hash(password)