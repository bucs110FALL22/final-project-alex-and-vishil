import random
from src.logger import Logger
from src.bomb import Bomb
from src.character import MainCharacter


class GameModel:
    '''
    Game Model - holds all the data abou the state of the game.
    '''

    def __init__(self, num_of_lanes: int = 10) -> None:
        '''
        constructor
        num_of_lanes: (int) number of lanes in the game. Used to calculate object sizes and positions.
        '''
        self.num_of_lanes = num_of_lanes
        self.score = 0
        self.max_score = 0
        self.is_over = False
        self.start_game()

    def start_game(self):
        '''
        Starts the game - resets the state for a new round.
        '''
        self.grab_max_score()
        self.reset_score()
        self.init_character()
        self.init_bombs()

    def grab_max_score(self):
        '''
        Sets max score since the game was instantiated.
        '''
        self.max_score = max(self.score, self.max_score)

    def reset_score(self):
        '''
        Resets the score and 
        '''
        self.is_over = False
        self.score = 0

    def init_character(self):
        '''
        Initializes the main character
        '''
        self.character = MainCharacter(self.num_of_lanes)

    def init_bombs(self):
        '''
        Initializes the falling bombs
        '''
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

    def update_data(self):
        '''
        Model Update - called to advance the game. Updates the model on each call.
        '''
        self.drop_bombs()
        self.check_for_collisions()
        self.check_for_bombs_evaded()
        if self.character.is_dead():
            self.end_game()

    def end_game(self):
        '''
        Ends the game
        '''
        self.is_over = True

    def drop_bombs(self):
        '''
        Uopdates the bombs models to simulate falling
        '''
        for bomb in self.bombs:
            bomb.drop()

    def move_character_left(self):
        '''
        Updates the position of the main character to move it to the left.
        '''
        self.character.move_left()

    def move_character_right(self):
        '''
        Updates the position of the main character to move it to the right.
        '''
        self.character.move_right()

    def check_for_collisions(self):
        '''
        Dectecs collisions between the character and the falling objects like bombs
        '''
        for bomb in self.bombs:
            if self.is_hit(bomb):
                bomb.set_state_target_hit()
                self.character.loose_life()

    def check_for_bombs_evaded(self):
        '''
        Checks for bombs that reached the bottom and did not hit the character. 
        Increases the game score accordingly.
        '''
        for bomb in self.bombs:
            if self.is_evaded(bomb):
                bomb.set_state_evaded()
                self.score += bomb.score_value

    def is_hit(self, bomb: Bomb) -> bool:
        '''
        Checks whether the input bomb hit the character.
        bomb: (Bomb) Bomb to check for collision.
        '''
        if not bomb.is_state_active():
            return False

        if bomb.lane != self.character.lane:
            return False

        bomb_bottom = bomb.bottom()
        return bomb_bottom >= self.character.top

    def is_evaded(self, bomb: Bomb) -> bool:
        '''
        Checks whether the input bomb reachedd the bottom without hitting the character.
        bomb: (Bomb) Bomb to check for collision.
        return: (bool) True if the bomb was evaded
        '''
        if not bomb.is_state_active():
            return False

        character_height_percent = 90
        reached_bottom = bomb.log_depth >= character_height_percent

        if not reached_bottom:
            return False

        return bomb.lane != self.character.lane
