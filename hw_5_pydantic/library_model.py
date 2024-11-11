from pydantic import BaseModel, field_validator


class Book(BaseModel):
    title: str
    author: str
    year: int
    available: bool


class User(BaseModel):
    name: str
    email: str
    membership_id: str

    @field_validator("email")
    def email_must_contain_atsign_symbol(cls, v):
        if "@" not in v:
            raise ValueError("email must contain @ symbol")
        return v
