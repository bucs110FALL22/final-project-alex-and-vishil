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
        self.set_state_active()
        self.score_value = score_value

    def reset(self):
        '''
        Restores the bomb data.
        '''
        self.log_depth = 0
        self.set_state_active()

    def drop(self):
        '''
        Updates the position of the bomb vertically according to the speed
        '''
        full_height = 100
        new_height = self.log_depth + self.speed
        if new_height >= full_height:
            self.reset()
        self.log_depth = new_height % full_height

    def bottom(self) -> float:
        '''
        Returns the logical vertical coordinate of the bottom of the bomb
        return: (float) logical vertical coordinates
        '''
        return self.log_depth + self.log_height

    def is_visible(self) -> bool:
        '''
        Is the bomb visible
        return: (bool) True if the bomb is visible
        '''
        return self.visible

    def set_state_active(self):
        '''
        Sets the bomb state to active. 
        This is the state while the bomb is falling
        '''
        self.state = 'active'

    def set_state_evaded(self):
        '''
        Sets the bomb state to evaded.
        This is the state for a bomb that reached the bottom without hiting the character
        '''
        self.state = 'evaded'

    def set_state_target_hit(self):
        '''
        Sets the bomb state to target-hit.
        This is the state for a bomb that hit the character
        '''
        self.state = 'target_hit'

    def is_state_active(self) -> bool:
        '''
        return: (bool) True if the bomb state is active.
        '''
        return self.state == 'active'

    def is_state_evaded(self) -> bool:
        '''
        return: (bool) True if the bomb state is evaded.
        '''
        return self.state == 'evaded'

    def is_state_target_hit(self) -> bool:
        '''
        return: (bool) True if the bomb state is target_hit.
        '''
        return self.state == 'target_hit'