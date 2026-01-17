class Car:
    def __init__(self) -> None:
        self.__fuel = 100

    # regular get set

    # def get_fuel(self):
    #     return self.fuel

    # def set_fuel(self, new_fuel):
    #     self.fuel = new_fuel

    # pythonic get set
    @property
    def fuel(self):
        print("using setter!")
        return self.__fuel

    @fuel.setter
    def fuel(self, new_fuel):
        print("using getter!")
        self.__fuel = new_fuel


# regular get set usage
# c = Car()
# print(c.get_fuel())
# c.set_fuel(100)
# print(c.get_fuel())

# pythonic
c = Car()
# use get
print(c.fuel)  # looks like a field - but this is a method
c.fuel = 100  # looks like var setting - but this is a method
print(c.fuel)  # looks like a field - but this is a method
