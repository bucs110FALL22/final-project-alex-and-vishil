import pygame

from src.display import Display
from src.gameoverscreen import GameoverScreen
from src.gamescreen import GameScreen
from src.welcomescreen import WelcomeScreen

DISPLAY_WIDTH = 1200
DISPLAY_HEIGHT = 1000
NUM_OF_LANES: int = 10


class Controller:

    def __init__(self):
        # setup pygame data
        self.display = Display(width=DISPLAY_WIDTH, height=DISPLAY_HEIGHT, num_of_lanes=NUM_OF_LANES)
        self._running = True
        self.is_debug = False
        self._app_state = 'welcome'
        self.welcome_screen = WelcomeScreen(self.display)
        self.game_screen = GameScreen(self.display)
        self.gameover_screen = GameoverScreen(self.display)
        self.clock = pygame.time.Clock()
        self.counter = 0

    def mainloop(self):
        # select state loop
        while self._running:
            self.counter += 1
            if self.is_debug:
                print('counter = ' + str(self.counter))
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
        self.game_screen.gamelogic_tick()

        # redraw
        self.display.draw_background()
        self.diplay_game()
        # self.clock.tick(10)  # controls game speed.
        pygame.display.flip()
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

    def diplay_game(self):
        self.game_screen.draw()

    def diplay_gameover(self):
        self.gameover_screen.draw()

    def start_game(self):
        self._app_state = 'game-on'

    def end_game(self):
        self._app_state = 'game-over'

    def handle_global_events(self, event):
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

    def handle_welcome_screen_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_SPACE]:
                self.start_game()

    def handle_game_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_o]:
                self.end_game()
                return
        self.game_screen.handle_game_events(event)

    def handle_gameover_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_SPACE]:
                self.start_game()
