import pygame

from src.display import Display
from src.gameoverscreen import GameoverScreen
from src.welcomescreen import WelcomeScreen


class Controller:

	def __init__(self):
		# setup pygame data
		self.display = Display()
		self._running = True
		self.is_debug = True
		self._app_state = 'welcome'
		self.welcome_screen = WelcomeScreen(self.display)
		self.gameover_screen = GameoverScreen(self.display)

	def mainloop(self):
		# select state loop
		while self._running:
			if self._app_state == 'welcome':
				self.menuloop()
			elif self._app_state == 'game-on':
				self.gameloop()
			elif self._app_state == 'game-over':
				self.gameoverloop()

	# below are some sample loop states #

	def menuloop(self):
		# event loop
		for event in pygame.event.get():
			self.handle_global_events(event)
			self.handle_welcome_screen_events(event)

		# update data

		# redraw
		self.display.draw_background()
		self.diplay_welcome()
		pygame.display.update()

	def gameloop(self):
		# event loop
		for event in pygame.event.get():
			self.handle_global_events(event)
			self.handle_game_events(event)

		# update data

		# redraw
		self.display.draw_background()
		pygame.display.update()

	def gameoverloop(self):
		# event loop
		for event in pygame.event.get():
			self.handle_global_events(event)
			self.handle_gameover_events(event)

		# update data

		# redraw
		self.display.draw_background()
		self.diplay_gameover()
		pygame.display.update()

	def handle_global_keyboard_event(self, event):
		if event.type != pygame.KEYDOWN:
			return
		if event.key in [pygame.K_s]:
			pass
		if event.key in [pygame.K_g]:
			self.is_debug = not self.is_debug
		if event.key in [pygame.K_q]:
			self.exit_app()

	def diplay_welcome(self):
		self.welcome_screen.draw()

	def diplay_gameover(self):
		self.gameover_screen.draw()

	def start_game(self):
		self._app_state = 'game-on'

	def end_game(self):
		self._app_state = 'game-over'

	def handle_global_events(self, event):
		self.check_and_quit_app_if_needed(event)
		self.handle_global_keyboard_event(event)

	def check_and_quit_app_if_needed(self, event):
		if (event.type == pygame.QUIT):
			self.exit_app()

	def exit_app(self):
		self._running = False
		pygame.quit()
		raise SystemExit

	def handle_welcome_screen_events(self, event):
		if event.type == pygame.KEYDOWN:
			if event.key in [pygame.K_SPACE]:
				self.start_game()

	def handle_game_events(self, event):
		if event.type == pygame.KEYDOWN:
			if event.key in [pygame.K_o]:
				self.end_game()

	def handle_gameover_events(self, event):
		if event.type == pygame.KEYDOWN:
			if event.key in [pygame.K_SPACE]:
				self.start_game()
