# basic polymorphims


class Bird:
    def __init__(self, name) -> None:
        self.name = name
        self.has_wings = True

    def fly(self):
        print("i am a bird and i fly!!!")


class Eagle(Bird):
    def __init__(self, name) -> None:
        super().__init__(name)

    def fly(self):
        print("i am an eagle and i fly!!!")


bird1 = Bird("bird1")
bird1.fly()

golden_eagle = Eagle("golden eagle")
golden_eagle.fly()
