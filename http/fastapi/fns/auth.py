from fns.db_ops import load_db

def validate_creds(username, password):
    db = load_db()
    stored_user = db[0]
    if stored_user["username"] == username and stored_user["password"] == password:
        return True
    return False

