from passlib.context import CryptContext


class Hash:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @classmethod
    def get_password_hash(cls, password: str) -> str:
        """This method hashes the given password and returns the hash."""
        return cls.pwd_context.hash(password)

    @classmethod
    def verify_password(cls, plain_password: str, hashed_password: str) -> bool:
        """This method verifies the given plain password with the given hashed password."""
        return cls.pwd_context.verify(plain_password, hashed_password)
