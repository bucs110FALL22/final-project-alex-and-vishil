import random
import pygame
from src.bomb import Bomb
from src.image import Image
from src.display import Display
from src.pygame_helpers import Helpers
from src.character import MainCharacter
from src.assets import Assets


class GameScreen:

    def __init__(self, display: Display) -> None:
        self.helper = Helpers()
        self.display = display
        self.init_character()
        self.init_bombs()

    def init_character(self):
        self.character = MainCharacter(self.display.NUM_OF_LANES)
        self.character_image = Image(Assets.images.get('character'),
                                     self.display.lane_width,
                                     self.display.lane_width)

    def init_bombs(self):
        self.bombs: list[Bomb] = []
        for i_lane in range(self.display.NUM_OF_LANES):
            rand = random.randint(0, self.display.NUM_OF_LANES)
            bomb = Bomb(self.display.NUM_OF_LANES,
                        speed=(rand / 2) + 1,
                        lane=i_lane,
                        damage=0,
                        score_value=0)
            self.bombs.append(bomb)
        self.bomb_image = Image(Assets.images.get('bomb'),
                                self.display.lane_width,
                                self.display.lane_width)

    def draw(self):
        self.display_game()

    def display_game(self):
        self.draw_character()
        self.draw_bombs()

    def handle_game_events(self, event):
        if event.type != pygame.KEYDOWN:
            return
        if event.key in [pygame.K_a, pygame.K_LEFT]:
            self.character.move_left()
        elif event.key in [pygame.K_d, pygame.K_RIGHT]:
            self.character.move_right()

    def draw_character(self):
        x_character = self.display.lane_width * self.character.lane
        y_character = self.display.height - self.display.lane_width
        self.character_image.draw(self.display.surface, x_character,
                                  y_character)

    def draw_bombs(self):
        for bomb in self.bombs:
            x_bomb = bomb.lane * self.display.lane_width
            y_bomb = bomb.height * self.display.height / 100
            self.bomb_image.draw(self.display.surface, x_bomb, y_bomb)

    def gamelogic_tick(self):
        for bomb in self.bombs:
            bomb.drop()
