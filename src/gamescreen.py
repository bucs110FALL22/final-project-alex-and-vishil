import pygame
from src.image import Image
from src.display import Display
from src.pygame_helpers import Helpers
from src.game_model import GameModel
from src.assets import Assets


class GameScreen:

    def __init__(self, display: Display) -> None:
        self.helper = Helpers()
        self.display = display
        self.game_model = GameModel()
        self.init_character_image()
        self.init_bomb_image()

    def init_character_image(self):
        self.character_image = Image(Assets.images.get('character'),
                                     self.display.lane_width,
                                     self.display.lane_width)

    def init_bomb_image(self):
        self.bomb_image = Image(Assets.images.get('bomb'),
                                self.display.lane_width,
                                self.display.lane_width)

    def draw(self):
        self.display_game()

    def display_game(self):
        self.draw_scoreboard()
        self.draw_character()
        self.draw_bombs()

    def handle_game_events(self, event):
        if event.type != pygame.KEYDOWN:
            return
        if event.key in [pygame.K_a, pygame.K_LEFT]:
            self.game_model.character.move_left()
        elif event.key in [pygame.K_d, pygame.K_RIGHT]:
            self.game_model.character.move_right()

    def draw_character(self):
        x_character = self.display.lane_width * self.game_model.character.lane
        y_character = self.display.height - self.display.lane_width
        self.character_image.draw(self.display.surface, x_character,
                                  y_character)

    def draw_bombs(self):
        for bomb in self.game_model.bombs:
            x_bomb = bomb.lane * self.display.lane_width
            y_bomb = bomb.height * self.display.height / 100
            self.bomb_image.draw(self.display.surface, x_bomb, y_bomb)

    def draw_scoreboard(self):
        pass

    def gamelogic_tick(self):
        self.game_model.gamelogic_tick()
