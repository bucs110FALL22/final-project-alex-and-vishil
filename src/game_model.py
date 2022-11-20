import random
from src.falling_object import FallingObject
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
        self.falling_objects: FallingObject[0] = []
        FallingObject.num_of_lanes = num_of_lanes
        self.start_game()

    def start_game(self):
        '''
        Starts the game - resets the state for a new round.
        '''
        self.grab_max_score()
        self.reset_score()
        self.init_character()
        self.init_falling_objects()

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

    def init_falling_objects(self):
        '''
        Initializes the falling objects
        '''
        self.falling_objects: list = []
        self.add_bomb_objects()
        self.add_life_objects()

    def add_bomb_objects(self):
        '''
        Adds 'bombs' falling objects to the list of falling objects
        '''
        for i_lane in range(self.num_of_lanes):
            obj = self.create_falling_object(type='bomb', i_lane=i_lane)
            self.falling_objects.append(obj)

    def add_life_objects(self):
        '''
        Adds 'life' falling objects to the list of falling objects
        '''
        num_of_life_objects = 2
        for i in range(num_of_life_objects):
            obj = self.create_falling_object(type='life', use_random_lane=True)
            self.falling_objects.append(obj)

    def create_falling_object(self,
                              type: str = '',
                              i_lane: int = 0,
                              use_random_lane: bool = False) -> FallingObject:
        '''
        Createst a single falling object depeding on the type.
        i_lane: (int) game lane to assign to the newly created object.
        use_random_lane: (bool) True to ignore the provided lane and use a random one instead
        type: (str) type of object being created.
        return: (FallingObject) created object
        '''
        min_speed = 5
        max_speed = 15
        falling_speed = random.randint(min_speed, max_speed) / 100
        value = int(falling_speed * 4 * 100)
        logical_height = 100 / self.num_of_lanes
        obj = FallingObject(type=type,
                            speed=falling_speed,
                            lane=i_lane,
                            use_random_lane=use_random_lane,
                            log_height=logical_height,
                            score_value=value)

        return obj

    def update_data(self):
        '''
        Model Update - called to advance the game. Updates the model on each call.
        '''
        self.drop_falling_objects()
        self.check_for_collisions()
        self.check_for_falling_objects_evaded()
        if self.character.is_dead():
            self.end_game()

    def end_game(self):
        '''
        Ends the game
        '''
        self.is_over = True

    def drop_falling_objects(self):
        '''
        Uopdates the falling objects models to simulate falling
        '''
        for obj in self.falling_objects:
            obj.drop()

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
        Dectecs collisions between the character and the falling objects like falling objects
        '''
        for obj in self.falling_objects:
            if self.is_hit(obj):
                obj.set_state_target_hit()
                if obj.is_bomb():
                    self.character.loose_life()
                elif obj.is_life():
                    self.character.add_life()
                    obj.lane = random.randint(0, self.num_of_lanes)

    def check_for_falling_objects_evaded(self):
        '''
        Checks for falling objects that reached the bottom and did not hit the character. 
        Increases the game score accordingly.
        '''
        for obj in self.falling_objects:
            if self.is_evaded(obj):
                obj.set_state_evaded()
                if obj.is_bomb():
                    self.score += obj.score_value

    def is_hit(self, obj: FallingObject) -> bool:
        '''
        Checks whether the input falling object hit the character.
        obj: (FallingObject) Falling object to check for collision.
        '''
        if not obj.is_state_active():
            return False

        if obj.lane != self.character.lane:
            return False

        obj_bottom = obj.bottom()
        return obj_bottom >= self.character.top

    def is_evaded(self, obj: FallingObject) -> bool:
        '''
        Checks whether the input falling object reachedd the bottom without hitting the character.
        obj: (FallingObject) Falling object to check for collision.
        return: (bool) True if the falling object was evaded
        '''
        if not obj.is_state_active():
            return False

        character_height_percent = 90
        reached_bottom = obj.log_depth >= character_height_percent

        if not reached_bottom:
            return False

        return obj.lane != self.character.lane
