class Scoreboard():
	'''
  Scoreboard represents the model for the information displayd regarding the 
  state of the game, including the score, lives, powerups, level, and high score
  '''

	def __init__(self,
	             rect,
	             score: int = 0,
	             level: int = 1,
	             lives: int = 0,
	             powerups: float = 0,
	             high_score: int = 0) -> None:
		'''
    Model for the game scoreboard. Holds the data to display on the screen.
    Does not inherit from Sprite
    rect: (str) character's rectangle in the display
    score: (int) game score
    level: (int) game level
    lives: (int) number of lives or strength the character has
    powerups: (float) factor of score increase
    high_score: (int) current highest score
    '''
		self.rect = rect
		self.score = score
		self.level = level
		self.lives = lives
		self.powerups = powerups
		self.high_score = high_score

	def reset(self):
		'''
    Resets the score, lives, and powerups. 
    '''
		self.score = 0
		self.level = 1
		self.lives = 3
		self.powerups = 0

	def set_score(self, new_score: int = 0):
		'''
    Sets the new score and updates the highest score if needed.
    new_score: (int) new game score
    '''
		self.score = new_score
		if new_score > self.high_score:
			self.high_score = new_score
