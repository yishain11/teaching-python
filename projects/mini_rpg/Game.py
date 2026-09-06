from Maze.Maze import Maze
from Charecters.Chars import available_player_types as player_types


class Game:
    def __init__(self) -> None:
        self.player_types = player_types
        self.show_gen_player_manu()
        self.maze = Maze()

    def show_gen_player_manu(self):
        print("welcome to the rpg!")
        print("please select player type: ")
        for i, p_type in enumerate(self.player_types):
            print(i, p_type.__name__)
        action = int(input("please select the type: "))
        while int(action) < 0 or int(action) >= len(self.player_types):
            print("bad input")
            action = int(input("please select the type: "))
        player = self.player_types[action](input(" select player name"))
        self.player = player

    def start_game(self):
        pass
