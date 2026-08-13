# store username
username = input("new username: ")
file = open("secret.txt", "w")
file.write(username)
file.close()


# check that username was written
file = open("secret.txt", "r")
print("file secret is: ", file.read())
file.close()


# append
name = input("what is your name? ")
file = open("name.txt", "a+")
file.write(name)
# read the file
print("name is: ", file.read())  # what is happening?
file.close()

# fix
name = input("what is your name? ")
file = open("name.txt", "a+")
file.write(name)
# read the file
file.seek(0)
print("name is: ", file.read())  # what is happening?
file.close()
