from random import randint

suits = ["D", "S", "C", "H"]
card_ranks = [str(x) for x in range(2, 11)]
card_ranks.append("J")
card_ranks.append("Q")
card_ranks.append("K")
card_ranks.append("A")


class Card:
    def __init__(self, rank, suit) -> None:
        self.rank = rank
        self.suit = suit
        self.gen_value()
        self.type = "regular"

    def gen_value(self):
        try:
            int_rank = int(self.rank)
            self.value = int_rank
        except:
            match self.rank.lower():
                case "j":
                    self.value = 11
                case "q":
                    self.value = 12
                case "k":
                    self.value = 13
                case "a":
                    self.value = 1

    def get_type(self):
        return self.rank + self.suit

    def get_value(self):
        return self.value


class Deck:
    def __init__(self) -> None:
        self.cards = []
        self.gen_regular_cards()
        self.shuffle_cards()

    def gen_regular_cards(self):
        for suit in suits:
            for rank in card_ranks:
                self.cards.append(Card(rank, suit))

    def special_cards(self):
        self.cards.append(BombCard())
        self.cards.append(JokerCard())

    def select_indices(self):
        index1 = randint(0, len(self.cards) - 1)
        index2 = randint(0, len(self.cards) - 1)
        while index1 == index2:
            index1 = randint(0, len(self.cards) - 1)
        return index1, index2

    def shuffle_cards(self):
        for _ in range(5000):
            index1, index2 = self.select_indices()
            card1 = self.cards[index1]
            self.cards[index1] = self.cards[index2]
            self.cards[index2] = card1

    def get_len_deck(self):
        return len(self.cards)

    def draw_card_from_deck(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        raise ValueError("not enough cards")

    def print_cards(self):
        for card in self.cards:
            print(card.get_type())


class Player:
    def __init__(self) -> None:
        self.name = None
        self.type = "regular"
        self.hand = []
        self.get_name()
        self.win_pile = []

    def get_name(self):
        name = input(" please enter your name ")
        while len(name) < 5 or len(name) > 10:
            print("name should be between 5-10 chars")
            name = input(" please enter your name ")
        self.name = name

    def draw_card(self):
        if len(self.hand) > 0:
            return self.hand.pop()
        raise ValueError(f"player {self.name} has no more cards")

    def add_card_to_hand(self, card):
        if isinstance(card, Card):
            self.hand.append(card)
            return
        raise ValueError

    def get_hand_len(self):
        return len(self.hand)

    def get_win_pile_len(self):
        return len(self.win_pile)

    def add_cards_to_win_pile(self, cards):
        for card in cards:
            self.win_pile.append(card)

    def decrease_win_pile(self):
        self.win_pile.pop()


class AdminPlayer(Player):
    def __init__(self) -> None:
        super().__init__()
        self.type = "admin"
        self.get_name()
        self.times_to_win_auto = 1

    def use_autowin_ability(self):
        if self.times_to_win_auto == 1:
            print("admin winning auto!")
            self.times_to_win_auto = 0
            return True
        print("you already used this ability")
        return False


class BombCard(Card):
    def __init__(self) -> None:
        super().__init__("B", "")
        self.type = "bomb"
        self.used = False

    def use_bomb(self, player):
        if not self.used:
            print("bomb used!")
            self.used = True
            player.decrease_win_pile()
        print("cannot use - already used!")


class JokerCard(Card):
    def __init__(self) -> None:
        super().__init__("J", "")
        self.type = "Joker"


class Game:
    def __init__(self) -> None:
        self.players = []
        self.deck = None

        for _ in range(2):
            self.gen_player()

        self.gen_deck()
        self.deal_cards()
        self.run_game()

    def gen_player(self):
        player_type = input(" what type of player you want to be? Admin/Regular - A/R ")
        while player_type.lower() not in ["a", "r"]:
            player_type = input(
                " wrong input. what type of player you want to be? Admin/Regular - A/R "
            )
        match player_type.lower():
            case "a":
                self.players.append(AdminPlayer())
            case "r":
                self.players.append(Player())

    def gen_deck(self):
        self.deck = Deck()

    def deal_cards(self):
        for _ in range(self.deck.get_len_deck() // 2):
            for player in self.players:
                player.add_card_to_hand(self.deck.draw_card_from_deck())

    def run_game(self):
        while self.players[0].get_hand_len() > 0 and self.players[1].get_hand_len() > 0:
            cards = (self.players[0].draw_card(), self.players[0].draw_card())
            print(f"player 1 {self.players[0].name} drew: {cards[0].get_type()}")
            print(f"player 2 {self.players[1].name} drew: {cards[1].get_type()}")
            if cards[0].type == "bomb":
                print("bomb card!")
                cards[0].use_bomb(self.players[0])
            if cards[0].type == "bomb":
                print("bomb card!")
                cards[0].use_bomb(self.players[0])
            if cards[0].type == "bomb" or cards[0].type == "bomb":
                continue
            if cards[0].get_value() > cards[1].get_value():
                print("player 1 wins this round!")
                self.players[0].add_cards_to_win_pile(cards)
            elif cards[1].get_value() > cards[0].get_value():
                print("player 2 wins this round!")
                self.players[1].add_cards_to_win_pile(cards)
            else:
                print("equal cards! ignoring")
        print("game over!")
        player1_result = self.players[0].get_win_pile_len()
        player2_result = self.players[1].get_win_pile_len()
        print(f"player 1 {self.players[0].name} result is: {player1_result}")
        print(f"player 2 {self.players[1].name} result is: {player2_result}")
        if player1_result == player2_result:
            print("its a draw!")
        elif player2_result > player1_result:
            print(f"player 2 {self.players[1].name} wins! ")
        else:
            print(f"player 1 {self.players[0].name} wins! ")


g = Game()
