import pygame

class Powerup (pygame.sprite.Sprite):
    '''
    Screen object representing a powerup, that is, an object that provides
    extra powers like more lives or ghost-mode to become transparent to bombs.
    '''
    def __init__(self, image, rect, type: str = 'extra-life') -> None:
        '''
        constructor
        image: (str) file name for the powerup image
        rect: (str) powerup's rectangle in the display
        type: (string) type of the powerup, for example, extra-life, ghost-mode
        '''
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = rect
        self.type = type
