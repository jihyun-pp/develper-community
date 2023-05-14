from pydantic import BaseModel, Field, validator


class RefreshToken(BaseModel):
    token: str = Field(..., description="Token")
    refresh_token: str = Field(..., description="Refresh token")


class VerifyToken(BaseModel):
    token: str = Field(..., description="Token")


class RequestCreateUser(BaseModel):
    email: str = Field(..., description="email")
    password1: str = Field(..., description="password")
    password2: str = Field(..., description="confirm password")
    nickname: str = Field(..., description="nickname")

    @validator('email', 'password1')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v

    @validator('password2')
    def password_match(cls, v, values):
        if 'password1' in values and v != values['password1']:
            raise ValueError('비밀번호가 일치하지 않습니다.')
        return v