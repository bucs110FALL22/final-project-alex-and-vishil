import random
from src.logger import Logger
from src.bomb import Bomb
from src.character import MainCharacter


class GameModel:

    def __init__(self, num_of_lanes: int = 10) -> None:
        self.num_of_lanes = num_of_lanes
        self.score = 0
        self.max_score = 0
        self.start_game()

    def start_game(self):
        self.reset_score()
        self.init_character()
        self.init_bombs()

    def reset_score(self):
        self.max_score = max(self.score, self.max_score)
        self.score = 0

    def init_character(self):
        self.character = MainCharacter(self.num_of_lanes)

    def init_bombs(self):
        self.bombs: list[Bomb] = []
        for i_lane in range(self.num_of_lanes):
            min_speed = 5
            max_speed = 15
            falling_speed = random.randint(min_speed, max_speed) / 100
            value = int(falling_speed * 4 * 100)
            logical_height = 100 / self.num_of_lanes
            bomb = Bomb(speed=falling_speed,
                        lane=i_lane,
                        log_height=logical_height,
                        score_value=value)
            self.bombs.append(bomb)

    def gamelogic_tick(self) -> bool:
        self.drop_bombs()
        self.check_for_collisions()
        self.check_for_bombs_evaded()
        if self.character.is_dead():
            return False
        return True

    def drop_bombs(self):
        for bomb in self.bombs:
            bomb.drop()

    def move_character_left(self):
        self.character.move_left()

    def move_character_right(self):
        self.character.move_right()

    def check_for_collisions(self):
        for bomb in self.bombs:
            if self.is_hit(bomb) and bomb.visible:
                bomb.visible = False
                bomb.exploded = True
                self.character.lives -= 1
                Logger.log('lives = ' + str(self.character.lives))

    def check_for_bombs_evaded(self):
        for bomb in self.bombs:
            if self.is_evaded(bomb) and bomb.visible:
                bomb.visible = False
                self.score += bomb.score_value

    def is_hit(self, bomb: Bomb) -> bool:
        if bomb.exploded:
            return False

        if bomb.lane != self.character.lane:
            return False

        return bomb.bottom() >= self.character.top

        return bomb.lane == self.character.lane

    def is_evaded(self, bomb: Bomb) -> bool:
        character_height_percent = 90
        if bomb.log_depth <= character_height_percent or bomb.exploded:
            return False

        bomb.exploded = True
        return True
