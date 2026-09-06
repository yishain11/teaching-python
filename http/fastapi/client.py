import requests as req


def client_main():
    action = input("action? ")
    if action == "get":
        username = input("username ")
        password = input("password ")
        result = req.post(
            "http://127.0.0.1:8000/users/1",
            json={"username": username, "password": password},
        )
        json_response = result.json()
        print(f"result is: {json_response}")


client_main()
