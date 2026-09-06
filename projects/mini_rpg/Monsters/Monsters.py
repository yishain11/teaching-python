import config as C
from random import randint as ri


class BaseMonster:
    def __init__(self, name) -> None:
        self.name = name
        self.power = ri(2, 10)
        self.speed = ri(1, 10)
        self.luck = ri(1, 10)
        self.gold = ri(10, 50)
        self.life = C.MONSTER_BASE_LIFE


class Ork(BaseMonster):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.name += " the ork"
        self.power += C.ORK_POWER_BONUS
        self.speed -= C.ORK_SPEED_DECREMENT
        self.life = C.ORK_LIFE


class Goblin(BaseMonster):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.name += " the goblin"
        self.power -= C.GOBLIN_POWER_DECREMENT
        self.speed += C.GOBLIN_SPEED_BONUS
        self.life = C.ORK_LIFE
        self.gold += C.GOBLIN_GOLD_BONUS


monsters_class = [Ork, Goblin]
