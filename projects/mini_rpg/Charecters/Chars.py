import config as c


class BaseChar:
    def __init__(self, name) -> None:
        self.name = name
        self.life = c.PLAYER_TOTAL_LIFE
        self.power = 0
        self.speed = 0
        self.luck = 0
        self.max_potions = c.MAX_POTIONS_TO_CARRY
        self.current_potions = c.STARTING_PLAYER_POTION_NUM
        self.alocate_points()

    def alocate_points(self):
        self.power = 20
        self.speed = 20
        self.luck = 20


class Figher(BaseChar):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.power += c.FIGHTER_POWER_BONUS
        self.damage_bonus = c.FIGHTER_DAMAGE_BONUS
        self.max_potions += c.FIGHTER_POTION_CARRY_BONUS
        self.speed -= c.FIGHTER_SPEED_DECREMENT


class Wizard(BaseChar):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.max_potions -= c.WIZARD_POTION_CARRY_DECREMENT


class Theif(BaseChar):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.power -= c.THIEF_POWER_DECREMENT
        self.speed += c.THIEF_SPEED_BONUS
        self.gold_bonus = c.THIEF_GOLD_BONUS


available_player_types = [Figher, Theif, Wizard]
