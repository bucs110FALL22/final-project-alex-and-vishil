import pygame


class Bomb(pygame.sprite.Sprite):
	'''
  Screen object representing a lethal bomb that reduced the number of character lifes and has a score value that corresponds to the score increase when the character avoids it.
  '''

	def __init__(self,
	             image,
	             rect,
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
		pygame.sprite.Sprite.__init__(self)
		self.image = image
		self.rect = rect
		self.speed = speed
		self.damage = damage
		self.score_value = score_value

	def drop(self):
		'''
    Updates the position of the bomb vertically according to the speed
    '''
		pass
