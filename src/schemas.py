from pydantic import BaseModel
from typing import List


class User(BaseModel):
    id: int
    name: str
    username: str
    email: str

    class Config:
        orm_mode = True


class ListUserResponse(BaseModel):
    status: str
    results: int
    users: List[User]
