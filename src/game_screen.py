from src.scoreboard import Scoreboard
from src.game_controller import GameController
from src.image import Image
from src.display import Display
from src.helper import Helper
from src.game_model import GameModel
from src.assets import Assets


class GameScreen:

    def __init__(self, display: Display) -> None:
        self.helper = Helper()
        self.display = display
        self.game_model = GameModel()
        self.game_controller = GameController(self.game_model)
        self.scoreboard = Scoreboard(display)
        self.init_character_image()
        self.init_bomb_image()

    def start(self):
        self.game_model.start_game()

    def init_character_image(self):
        width = self.display.lane_width
        height = self.display.lane_width
        image_file = Assets.images.get('character')
        self.character_image = Image(image_file, width, height)

    def init_bomb_image(self):
        width = self.display.lane_width
        height = self.display.lane_width
        image_file = Assets.images.get('bomb')
        self.bomb_image = Image(image_file, width, height)

    def draw(self):
        self.display_game()

    def display_game(self):
        self.draw_scoreboard()
        self.draw_character()
        self.draw_bombs()

    def draw_character(self):
        x_character = self.display.lane_width * self.game_model.character.lane
        y_character = self.display.height * (
            100 - self.game_model.character.height) / 100
        self.character_image.draw(self.display.surface, x_character,
                                  y_character)

    def draw_bombs(self):
        for bomb in self.game_model.bombs:
            x_bomb = bomb.lane * self.display.lane_width
            y_bomb = bomb.log_depth * self.display.height / 100
            if not bomb.exploded:
                self.bomb_image.draw(self.display.surface, x_bomb, y_bomb)
            else:
                x_bomb = x_bomb + self.display.lane_width / 2
                font_size = 40
                self.helper.print(self.display.surface, str(bomb.score_value),
                                  font_size, (x_bomb, y_bomb))

    def draw_scoreboard(self):
        self.scoreboard.draw(self.game_model.character.lives,
                             self.game_model.score, self.game_model.max_score)

    def gamelogic_tick(self) -> bool:
        return self.game_model.gamelogic_tick()
