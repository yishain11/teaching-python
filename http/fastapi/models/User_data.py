from pydantic import BaseModel


class User_Data(BaseModel):
    username: str
    password: str


def print_upper(data):
    print(data.upper())
