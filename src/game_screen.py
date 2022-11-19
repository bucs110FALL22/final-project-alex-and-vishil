from src.game_controller import GameController
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
        self.game_controller = GameController(self.game_model)
        self.init_character_image()
        self.init_bomb_image()
        self.init_health_image()

    def start(self):
        self.game_model.start_game()

    def init_character_image(self):
        width = self.display.lane_width
        height = self.display.lane_width
        self.character_image = Image(Assets.images.get('character'), width,
                                     height)

    def init_bomb_image(self):
        width = self.display.lane_width
        height = self.display.lane_width
        self.bomb_image = Image(Assets.images.get('bomb'), width, height)

    def init_health_image(self):
        width = self.display.lane_width / 2
        height = self.display.lane_width / 2
        self.health_image = Image(Assets.images.get('health'), width, height)

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
            y_bomb = bomb.top * self.display.height / 100
            if not bomb.exploded:
                self.bomb_image.draw(self.display.surface, x_bomb, y_bomb)
            else:
                x_bomb = x_bomb + self.display.lane_width / 2
                self.helper.display_text(self.display.surface,
                                         str(bomb.score_value), 40,
                                         (x_bomb, y_bomb))

    def draw_scoreboard(self):
        margin = self.display.lane_width / 2
        for live in range(self.game_model.character.lives):
            x_health = margin + margin * live
            y_health = margin
            self.health_image.draw(self.display.surface, x_health, y_health)

        x_score = self.display.width / 2
        y_score = margin
        text_score = 'Score: ' + str(self.game_model.character.score)
        self.helper.display_text(self.display.surface, text_score, 30,
                                 (x_score, y_score))

    def gamelogic_tick(self) -> bool:
        return self.game_model.gamelogic_tick()
