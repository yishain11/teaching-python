class SimplerWorker:
    def __init__(self, name) -> None:
        self.__name = name
        self._age = 37
        pass

    def get_name(self):
        return self.__name

    def get_age(self):
        return self._age


# sw1 = SimplerWorker("yishai")
# print(sw1.__dict__)
# print(sw1.get_name())

# tsw.upper_case_name()


class TechSimplerWorker(SimplerWorker):
    def __init__(self, name) -> None:
        super().__init__(name)

    def upper_case_name(self):
        print(self.__name.upper())

    def minus1_age(self):
        print(self._age - 1)


tsw = TechSimplerWorker("bob")
print(tsw.__dict__)
tsw.minus1_age()
# tsw.upper_case_name()
