from Utils import Utils


class Player:
    def __init__(self, name) -> None:
        self.__name = name
        self.__num_of_wins = 0

    @property
    def name(self):
        return self.__name

    @property
    def num_of_wins(self):
        return self.__num_of_wins

    def add_1_win(self):
        self.__num_of_wins += 1

    def select(self):
        return Utils.select_rand_option()
