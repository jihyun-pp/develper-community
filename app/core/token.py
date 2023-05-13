from datetime import datetime, timedelta
import jwt
from app.core.env import environ
from app.core.exceptions import DecodeTokenException, ExpiredTokenException

class Token:
    @staticmethod
    def encode(payload: dict, expire_period: int = 3600*24) -> str:
        token = jwt.encode(
            payload={
                **payload,
                "exp": datetime.utcnow() + timedelta(seconds=expire_period),
            },
            key=environ('JWT_SECRET_KEY'),
            algorithm=environ('JWT_ALGORITHM'),
        ).decode("utf8")
        return token

    @staticmethod
    def decode(token: str) -> dict:
        try:
            return jwt.decode(token, environ('JWT_SECRET_KEY'), environ('JWT_ALGORITHM'))
        except jwt.exceptions.DecodeError:
            raise DecodeTokenException
        except jwt.exceptions.ExpiredSignatureError:
            raise ExpiredTokenException

    @staticmethod
    def decode_expired_token(token: str) -> dict:
        try:
            return jwt.decode(token, environ('JWT_SECRET_KEY'), environ('JWT_ALGORITHM'))
        except jwt.exceptions.DecodeError:
            raise DecodeTokenException