from src.display import Display
from src.pygame_helpers import Helpers


class GameoverScreen:

	def __init__(self, display: Display) -> None:
		self.helper = Helpers()
		self.display = display

	def draw(self):
		self.display_game_over()

	def display_game_over(self):
		x_text = self.display.width / 2
		y = self.display.height / 2 - 50
		self.helper.display_text(self.display.surface, 'Game Over', 100, (x_text, y))
		self.helper.display_text(self.display.surface, 'Press SPACE to start', 50,
		                         (x_text, y + 100))
