from random import randint, choice
import config as C
from Monsters.Monsters import monsters_class as MC


class Maze:
    def __init__(self) -> None:
        self.rooms = []
        self.rooms_num = 0
        self.total_monsters = 0
        self.init_maze()

    def gen_rooms(self):
        while self.rooms_num < C.MAZE_MIN_ROOM_NUM:
            room = Room(self.rooms_num)
            self.add_room(room)

    def init_maze(self):
        self.gen_rooms()
        self.update_room_num()
        while self.total_monsters <= C.MAZE_MIN_MONSTER_NUM:
            self.populate_rooms()
            self.sum_total_monsters_from_rooms()

    def add_room(self, room):
        if isinstance(room, Room):
            self.rooms.append(room)
            self.update_room_num()

    def update_room_num(self):
        self.rooms_num = len(self.rooms)

    def populate_rooms(self):
        for room in self.rooms:
            chance = randint(0, 1)
            if chance < C.MAZE_CHANCE_GEN_MONSTER:
                monster = choice(MC)(input(" give monster name "))
                room.add_monster(monster)
            else:
                potion_chance = randint(0, 1)
                if potion_chance <= 0.5:
                    room.has_potion = True
                    room.num_of_potions = randint(1, 2)

    def sum_total_monsters_from_rooms(self):
        total = 0
        for room in self.rooms:
            if room.report_has_monster:
                total += 1
        self.total_monsters = total


class Room:
    def __init__(self, room_num) -> None:
        self.has_monster = False
        self.current_monster = None
        self.has_potion = False
        self.num_of_potions = 0
        self.room_num = room_num

    def add_monster(self, monster):
        self.current_monster = monster
        self.has_monster = True

    def report_has_monster(self):
        return self.has_monster
