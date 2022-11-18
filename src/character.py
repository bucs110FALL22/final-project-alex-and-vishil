class MainCharacter():
    '''
    Screen object representing the main game character.
    '''

    def __init__(self, num_of_lanes: int = 0) -> None:
        '''
        constructor
        image: (str) file name for the character image
        rect: (str) character's rectangle in the display
        health: (int) number of lives or strength the character has
        powerups: (float) factor of score increase
        lane: (int) vertical lane where the character appears
        '''
        self.image = 'character'
        self.num_of_lanes = num_of_lanes
        self.lane = num_of_lanes / 2
        self.visible = True

    def increase_health(self, delta: int = 1):
        '''
        Increaces the character's number of lives by n
        delta: (int) increase in number of lives
        '''
        self.health += delta

    def decrease_health(self, delta: int = -1):
        '''
        Decreaces the character's number of lives by n
        delta: (int) decrease in number of lives
        '''
        self.powerups -= delta

    def increase_powerups(self, delta: int = 1):
        '''
        Increaces the character's number of powerups by n
        delta: (int) increase in number of powerups
        '''
        self.powerups += delta

    def decrease_powerups(self, delta: int = 1):
        '''
        Decreaces the character's number of powerups by n
        delta: (int) decrease in number of powerups
        '''
        self.powerups -= delta

    def move_right(self):
        '''
        Moves the character lane by one to the right.
        '''
        self.lane = (self.lane + 1) % self.num_of_lanes

    def move_left(self):
        '''
        Moves the character lane by one to the left.
        '''
        self.lane = (self.lane - 1) % self.num_of_lanes
