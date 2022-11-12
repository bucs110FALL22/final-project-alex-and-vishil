import pygame


class MainCharacter(pygame.sprite.Sprite):
  '''
  Screen object representing the main game character.
  '''

  def __init__(self,
               image,
               rect,
               health: int = 0,
               powerups: float = 0,
               lane: int = 0) -> None:
    '''
    constructor
    image: (str) file name for the character image
    rect: (str) character's rectangle in the display
    health: (int) number of lives or strength the character has
    powerups: (float) factor of score increase
    lane: (int) vertical lane where the character appears
    '''
    pygame.sprite.Sprite.__init__(self)
    self.image = image
    self.rect = rect
    self.health = health
    self.powerups = powerups
    self.lane = lane
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

  def move_right(self, delta: int = 1):
    '''
    Moves the character lane by one to the right.
    delta: (int) number of lanes to move.
    '''
    self.lanes += delta

  def move_left(self, delta: int = 1):
    '''
    Moves the character lane by one to the left.
    delta: (int) number of lanes to move.
    '''
    self.lanes -= delta
