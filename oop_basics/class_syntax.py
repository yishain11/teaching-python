# # basic class
# class Person:
#     pass


# # class with props
# class Pesron:
#     name = "bob"


# # class with methods
# class Peson:
#     name = "bob"

#     def say_name():
#         print(name)


# # instances
# class Person:
#     has_kids = False


# bob = Person()
# print(bob.has_kids)


# self
# class Person:
#     name = "bob"

#     def say_name():
#         print(name)


# bob = Person()
# bob.say_name()


# self fix
# class Person:
#     name = "bob"

#     def say_name(self):
#         print(self.name)


# bob = Person()
# bob.say_name()


# params
# class Person:
#     name = "bob"

#     def say_name(self):
#         print(self.name)

#     def update_name(self, new_name):
#         self.name = new_name


# bob = Person()
# bob.say_name()
# bob.update_name("BOB!!!")
# bob.say_name()


# constructor:
# class Person:
#     def __init__(self):
#         pass


# construtor with params
class Person:
    def __init__(self, name):
        self.name = name

    def say_name(self):
        print(self.name)


bob = Person("bob")
bob.say_name()
alice = Person("alice")
alice.say_name()
