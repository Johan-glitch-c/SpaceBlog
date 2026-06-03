from wsgiref import validate

from pydantic import BaseModel, EmailStr, Field,model_validator


class UserForm(BaseModel):
    username: str = Field(min_length=3, max_length=150)
    email: EmailStr
    password1: str = Field(min_length=8)
    password2: str

    @model_validator(mode='after')
    def passwords_match(self):
        if self.password1 != self.password2:
            raise ValueError("Passwords don't match")
        return self