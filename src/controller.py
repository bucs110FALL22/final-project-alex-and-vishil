import pygame
from src.game import Game
from src.logger import Logger
from src.display import Display
from src.gameover_screen import GameoverScreen
from src.welcome_screen import WelcomeScreen

DISPLAY_WIDTH: int = 1200
DISPLAY_HEIGHT: int = 1000
NUM_OF_LANES: int = 10
NUM_OF_ROWS: int = 10

Logger()


class Controller:

    def __init__(self):
        # setup pygame data
        self.display = Display(width=DISPLAY_WIDTH,
                               height=DISPLAY_HEIGHT,
                               num_of_lanes=NUM_OF_LANES)
        self.welcome_screen = WelcomeScreen(self.display)
        self.game = Game(self.display)
        self.gameover_screen = GameoverScreen(self.display)
        self.clock = pygame.time.Clock()
        self._running = True
        self.set_wecomescreen_state()

    def mainloop(self):
        # select state loop
        while self._running:
            if self.app_state == 'welcome':
                self.menuloop()
            elif self.app_state == 'game-on':
                self.gameloop()
            elif self.app_state == 'game-over':
                self.gameoverloop()

    def menuloop(self):
        # event loop
        for event in pygame.event.get():
            self.handle_global_event(event)
            self.handle_welcome_screen_event(event)

        # update data - No data to update

        # redraw
        self.display.draw_background()
        self.welcome_screen.draw()
        pygame.display.update()

    def gameloop(self):
        # event loop
        for event in pygame.event.get():
            self.handle_global_event(event)
            self.game.hangle_event(event)

        # update data
        self.game.update_data()
        if self.game.is_over():
            self.set_gameover_state()

        # redraw
        self.display.draw_background()
        self.game.draw()
        pygame.display.update()

    def gameoverloop(self):
        # event loop
        for event in pygame.event.get():
            self.handle_global_event(event)
            self.handle_gameover_event(event)

        # update data - No data to update

        # redraw
        self.display.draw_background()
        self.gameover_screen.draw()
        pygame.display.update()

    def handle_global_keyboard_event(self, event):
        if event.type != pygame.KEYDOWN:
            return
        if event.key in [pygame.K_s]:
            pass
        if event.key in [pygame.K_g]:
            Logger.is_debug = not Logger.is_debug
        if event.key in [pygame.K_q]:
            self.exit_app()

    def start_game(self):
        self.set_gameon_state()
        self.game.start()

    def end_game(self):
        self.set_gameover_state()

    def handle_global_event(self, event):
        if self.check_and_quit_app_if_needed(event):
            self.handle_global_keyboard_event(event)

    def check_and_quit_app_if_needed(self, event) -> bool:
        if (event.type == pygame.QUIT):
            self.exit_app()
            return False
        return True

    def exit_app(self):
        self._running = False
        pygame.quit()
        raise SystemExit

    def handle_welcome_screen_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_SPACE]:
                self.start_game()

    def handle_game_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_o]:
                self.end_game()
                return
        self.game_screen.game_controller.handle_game_events(event)

    def handle_gameover_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_SPACE]:
                self.start_game()

    def set_wecomescreen_state(self):
        self.app_state = 'welcome'

    def set_gameon_state(self):
        self.app_state = 'game-on'

    def set_gameover_state(self):
        self.app_state = 'game-over'
