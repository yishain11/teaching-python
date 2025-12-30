class IDF:
    def __init__(self) -> None:
        self.is_fighting = False
        pass

    soldiers_num = 5000

    def fight(self):
        print("figting!")
        self.is_fighting = True

    @staticmethod
    def stop_fighting():
        print("no fighting")


idf1 = IDF()
idf1.fight()
idf1.stop_fighting()
print(idf1.soldiers_num)
