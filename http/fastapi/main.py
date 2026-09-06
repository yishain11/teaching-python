from fastapi import FastAPI
from pydantic import BaseModel
from json import dumps, loads
from fns.auth import validate_creds
from fns.db_ops import search_user_by_id

app = FastAPI()


class Creds(BaseModel):
    username: str
    password: str


@app.get("/")
def fn():
    return {"msg": "hi"}


@app.post("/users/signin")
def store_new_users(creds: Creds):
    print(f"got body: {creds}")
    with open("db.json", "r+") as f:
        stored_data = loads(f.read())
        print("stored_data", stored_data)
        stored_data.append(creds.__dict__)
        f.write(dumps(stored_data))
        return {}


@app.post("/users/{id}")
def get_user_by_id(id, creds: Creds):
    print(f"creds: ", creds)
    # check username and password
    creds = creds.__dict__
    result = validate_creds(creds["username"], creds["password"])
    print("results is", result)
    # return given user if auth is ok
    user_search_result = search_user_by_id(id)
    return {"msg": f"result is: {user_search_result}"}
