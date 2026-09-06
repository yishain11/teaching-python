# no getter/setter


# class Person:
#     def __init__(self, name) -> None:
#         self.name = name

#     def set_name(self, new_name):
#         self.name = new_name

#     def get_name(self):
#         return self.name


# getter
class Person:
    def __init__(self, name) -> None:
        self.name = name

    def set_name(self, new_name):
        self.name = new_name

    @property
    def name(self):
        return self.name


p1 = Person("bob")
print(p1.name)
