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
        self.height = 15
        self.top = 100 - self.height
        self.visible = True
        self.lives = 3

    def is_dead(self) -> bool:
        '''
        Checks if the character is still alive
        return: (bool) True if it is still alive
        '''
        return self.lives <= 0

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
