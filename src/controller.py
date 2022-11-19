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
    '''
    Main application controller
    '''

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
        '''
        Main application loop for handling events and displaying content
        '''
        # select state loop
        while self._running:
            if self.app_state == 'welcome':
                self.menuloop()
            elif self.app_state == 'game-on':
                self.gameloop()
            elif self.app_state == 'game-over':
                self.gameoverloop()

    def menuloop(self):
        '''
        Welcome screen loop
        '''
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
        '''
        Game loop for handling user events and displaying the game.
        '''
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
        '''
        Game over screen loop - handles user input and displays instructions
        '''
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
        '''
        Handles keyboard events that are available globally in the application.
        '''
        if event.type != pygame.KEYDOWN:
            return
        if event.key in [pygame.K_s]:
            pass
        if event.key in [pygame.K_g]:
            Logger.is_debug = not Logger.is_debug
        if event.key in [pygame.K_q]:
            self.exit_app()

    def start_game(self):
        '''
        Starts the game
        '''
        self.set_gameon_state()
        self.game.start()

    def end_game(self):
        '''
        Ends the game
        '''
        self.set_gameover_state()

    def handle_global_event(self, event):
        '''
        Handles global input events. For example, applicaiton being closed.
        '''
        self.check_and_quit_app_if_needed(event)
        self.handle_global_keyboard_event(event)

    def check_and_quit_app_if_needed(self, event):
        '''
        Checks if the user chose to quic the app and cleans up.
        '''
        if (event.type == pygame.QUIT):
            self.exit_app()

    def exit_app(self):
        '''
        Exits the application cleanly
        '''
        self._running = False
        pygame.quit()
        raise SystemExit

    def handle_welcome_screen_event(self, event):
        '''
        Handles user input while the welcome screen is visible
        '''
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_SPACE]:
                self.start_game()

    def handle_gameover_event(self, event):
        '''
        Handles user input while the game over  screen is visible
        '''
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_SPACE]:
                self.start_game()

    def set_wecomescreen_state(self):
        '''
        Sets application state to show the Welcome Screen.
        '''
        self.app_state = 'welcome'

    def set_gameon_state(self):
        '''
        Sets application state to show the Game Screen.
        '''
        self.app_state = 'game-on'

    def set_gameover_state(self):
        '''
        Sets application state to show the Game Over Screen.
        '''
        self.app_state = 'game-over'
