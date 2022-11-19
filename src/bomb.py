class Bomb:
    '''
    Screen object representing a lethal bomb that reduced the number of character lifes and has a score value that corresponds to the score increase when the character avoids it.
    '''

    def __init__(self,
                 speed: float = 1,
                 lane: int = 0,
                 log_height: float = 15,
                 score_value: int = 0) -> None:
        '''
        constructor
        speed: (float) Vertical speed at which the bomb drops
        lane: (int) vertical lane where the bomb moves down.
        log_height: (int) bomb height as percent of the game vertical area.
        score_value: (int) score increase gained by avoiding the bomb
        '''
        self.image = 'bomb'
        self.lane = lane
        self.log_depth = 0  # depth as percent of the game vertical area.
        self.log_height = log_height
        self.speed = speed
        self.visible = True
        self.exploded = False
        self.score_value = score_value

    def reset(self):
        '''
        Restores the bomb data.
        '''
        self.log_depth = 0
        self.visible = True
        self.exploded = False

    def drop(self):
        '''
        Updates the position of the bomb vertically according to the speed
        '''
        full_height = 100
        new_height = self.log_depth + self.speed
        if new_height >= full_height:
            self.reset()
        self.log_depth = new_height % full_height

    def bottom(self):
        return self.log_depth + self.log_height
