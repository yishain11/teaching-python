class Car:
    def __init__(self, brand) -> None:
        self.num_of_wheels = 4
        self.brand = brand

    def start(self):
        print("rrrrrr")


class Toyota(Car):
    def __init__(self, price) -> None:
        self.price = price
        super().__init__("toyta")


class Tesla(Car):
    def __init__(self, brand) -> None:
        super().__init__(brand)

    def start(self):
        print("bzzzzz")


t1 = Toyota(34343)
tesla1 = Tesla("tesla")

t1.start()
tesla1.start()
