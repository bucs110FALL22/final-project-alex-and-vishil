class Bomb:
    '''
    Screen object representing a lethal bomb that reduced the number of character lifes and has a score value that corresponds to the score increase when the character avoids it.
    '''

    def __init__(self,
                 num_of_lanes: int = 0,
                 speed: float = 1,
                 lane: int = 0,
                 damage: int = 0,
                 score_value: int = 0) -> None:
        '''
        constructor
        image: (str) file name for the bomb image
        rect: (str) bomb rectangle in the display
        speed: (float) Vertical speed at which the bomb drops
        lane: (int) vertical lane where the bomb moves down.
        damage: (int) damage caused by the bomb on the character health.
        score_value: (int) score increase gained by the character when avoiding the bomb
        '''
        self.image = 'bomb'
        self.num_of_lanes = num_of_lanes
        self.lane = lane
        self.top = 0
        self.height = 100 / self.num_of_lanes
        self.speed = speed
        self.damage = damage
        self.visible = True
        self.exploded = False
        self.score_value = score_value

    def reset(self):
        self.visible = True
        self.exploded = False

    def drop(self):
        '''
        Updates the position of the bomb vertically according to the speed
        '''
        full_height = 100
        new_height = self.top + self.speed
        if new_height >= full_height:
            self.reset()
        self.top = new_height % full_height

    def bottom(self):
        return self.top + self.height
