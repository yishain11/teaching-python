import bcrypt

f = open("./data.txt", "r+")
cred_lines = f.readlines()
if len(cred_lines) < 2:
    username = input("username is: ")
    password = input("password is: ").encode()
    hashed_pass = bcrypt.hashpw(password, bcrypt.gensalt())
    f.write(f"{username}\n{hashed_pass.decode()}")
else:
    f.seek(0)
    loaded = f.readlines()
    username, password = loaded
    password_hashed = password.encode()
    print("username ", username, "password", password)
    given_usrname = input("username ")
    given_password = input("password ").encode()
    if bcrypt.checkpw(given_password, password_hashed):
        print("ok")
