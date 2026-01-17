from random import choice


class Utils:
    @staticmethod
    def select_rand_option(list_of_options=["rock", "paper", "scissors"]):
        return choice(list_of_options)

    @staticmethod
    def select_winner(player_1_choice, player_2_choice):
        match player_1_choice:
            case "rock":
                match player_2_choice:
                    case "rock":
                        return 0
                    case "paper":
                        return -1
                    case "scissors":
                        return 1
            case "paper":
                match player_2_choice:
                    case "rock":
                        return 1
                    case "paper":
                        return 0
                    case "scissors":
                        return -1
            case "scissors":
                match player_2_choice:
                    case "rock":
                        return -1
                    case "paper":
                        return 1
                    case "scissors":
                        return 0
