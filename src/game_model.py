import random
from src.bomb import Bomb
from src.character import MainCharacter


class GameModel:
    def __init__(self, num_of_lanes: int = 10) -> None:
        self.num_of_lanes = num_of_lanes
        self.init_character()
        self.init_bombs()

    def init_character(self):
        self.character = MainCharacter(self.num_of_lanes)

    def init_bombs(self):
        self.bombs: list[Bomb] = []
        for i_lane in range(self.num_of_lanes):
            min_speed = 5
            max_speed = 15
            falling_speed = random.randint(min_speed, max_speed)/100
            bomb = Bomb(self.num_of_lanes,
                        speed=falling_speed,
                        lane=i_lane,
                        damage=0,
                        score_value=0)
            self.bombs.append(bomb)

    def gamelogic_tick(self):
        self.drop_bombs()

    def drop_bombs(self):
        for bomb in self.bombs:
            bomb.drop()
