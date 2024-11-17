from pydantic import BaseModel, field_validator


class Book(BaseModel):
    title: str
    author: str
    year: int
    available: bool
    categories: list[str]

    @field_validator("categories")
    def categories_must_be_list(cls, v):
        if not isinstance(v, list):
            raise ValueError("categories must be a list")
        return v


class User(BaseModel):
    name: str
    email: str
    membership_id: str

    @field_validator("email")
    def email_must_contain_atsign_symbol(cls, v):
        if "@" not in v:
            raise ValueError("email must contain @ symbol")
        return v


class Library(BaseModel):
    books: list[Book]
    users: list[User]
