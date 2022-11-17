import os
import pygame
from src.assets import Assets
from src.image import Image


class Display:

	def __init__(self, width: int = 1200, height: int = 1000) -> None:
		self.width = width
		self.height = height

		self.fix_missing_display_error()
		self.setup_display_surface()

	def fix_missing_display_error(self):
		x = 100
		y = 0
		os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' % (x, y)

	def setup_display_surface(self):
		self.surface = pygame.display.set_mode((self.width, self.height))
		self.background_image = Image(Assets.images.get('background'), self.width,
		                              self.height)
		self.surface.fill('black')

	def draw_background(self):
		self.background_image.draw(self.surface, 0, 0)
