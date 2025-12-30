class Animal:
    def __init__(self, name, sound) -> None:
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} makes sound: {self.sound}")


class SeaAnimal(Animal):
    def __init__(self, name, sound, has_fins) -> None:
        super().__init__(name, sound)
        self.has_fins = has_fins

    def swim(self):
        print("im swimming!")


class Predator(Animal):
    def __init__(self, name, sound, has_strong_legs) -> None:
        super().__init__(name, sound)
        self.has_sharp_teeth = True
        self.has_strong_legs = has_strong_legs

    def bite(self):
        print("biting the pray")


class Shark(Predator, SeaAnimal):
    def __init__(self, name, sound) -> None:
        Predator.__init__(self, name, sound, True)
        SeaAnimal.__init__(self, name, sound, True)


s = Shark("bob", "blo blo blo")
print(s.has_fins)
