# no parent init


# class Person:
#     def say_hi(self):
#         print("hi")


# class Child(Person):
#     def __init__(self, name):
#         self.name = name

#     def say_name(self):
#         print(self.name)


# child1 = Child("bob")
# child1.say_name()
# child1.say_hi()


# inheritance - parent has constructor
# class Person:
#     def __init__(self, name) -> None:
#         self.name = name


# class Child(Person):
#     def __init__(self, age) -> None:
#         self.age = age


# child1 = Child(13)
# print(child1.name)  # ???


# fix - with super
class Person:
    def __init__(self, name) -> None:
        self.name = name


class Child(Person):
    def __init__(self, age, name) -> None:
        super().__init__(name)
        self.age = age


child1 = Child(13, "bob")
print(child1.name)  # bob


# class Person:
#     def __init__(self, age, name) -> None:
#         self.age = age
#         self.name = name

#     def say_name(self):
#         print("my name is ", self.name)


# class Teacher(Person):
#     def __init__(self, name) -> None:
#         self.name = name
#         super().__init__(43)


# t = Teacher("yishai")
# t.say_name()
