class Person:
    def __init__(self, age) -> None:
        self.age = age
        pass

    def say_name(self):
        print("my name is ", self.name)


class Teacher(Person):
    def __init__(self, name) -> None:
        self.name = name
        super().__init__(43)


t = Teacher("yishai")
t.say_name()
