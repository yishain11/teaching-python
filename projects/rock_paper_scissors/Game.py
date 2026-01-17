from Player import Player
from Utils import Utils


class Game:
    def __init__(self, rounds_to_win=10) -> None:
        self.__players = [Player("1"), Player("2")]
        self.__rounds_to_win = rounds_to_win
        self.__num_of_draws = 0

    def play_round(self):
        player_1_choice = self.__players[0].select()
        player_2_choice = self.__players[1].select()
        print(
            f"player 1 selected: {player_1_choice}\nplayer 2 selected: {player_2_choice}"
        )

        results = Utils.select_winner(player_1_choice, player_2_choice)
        match results:
            case 1:
                print("player 1 won this round!")
                self.__players[0].add_1_win()
                print(f"player 1 has {self.__players[0].num_of_wins} wins")
            case -1:
                print("player 2 won this round!")
                self.__players[1].add_1_win()
                print(f"player 2 has {self.__players[1].num_of_wins} wins")
            case 0:
                print("this round is a draw")
                self.__num_of_draws += 1
                print(f"now num of draws is: {self.__num_of_draws}")

    def play_game(self):
        while (
            self.__players[0].num_of_wins < self.__rounds_to_win
            and self.__players[1].num_of_wins < self.__rounds_to_win
        ):
            self.play_round()

        print("game is over.")
        print(f"player 1 wins: {self.__players[0].num_of_wins}")
        print(f"player 2 wins: {self.__players[1].num_of_wins}")
        msg = (
            "player 1 wins!"
            if self.__players[0].num_of_wins > self.__players[1].num_of_wins
            else "player 2 wins!"
        )
        print(msg)
        return
