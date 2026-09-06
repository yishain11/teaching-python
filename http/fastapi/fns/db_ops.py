from json import loads


def load_db():
    with open("db.json", "r") as f:
        stored_data = loads(f.read())
        return stored_data


def search_user_by_id(id):
    db = load_db()
    for user in db:
        if user["id"] == id:
            return user
    return False
