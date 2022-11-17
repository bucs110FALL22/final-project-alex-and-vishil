import pygame


class Helpers:

	def text_objects(self, text, font):
		textSurface = font.render(text, True, 'white')
		return textSurface, textSurface.get_rect()

	def display_text(self, surface, text, size, center):
		largeText = pygame.font.Font('freesansbold.ttf', size)
		TextSurf, TextRect = self.text_objects(text, largeText)
		TextRect.center = center
		surface.blit(TextSurf, TextRect)
