from src.display import Display
from src.pygame_helpers import Helpers


class GameScreen:

    def __init__(self, display: Display) -> None:
        self.helper = Helpers()
        self.display = display

    def draw(self):
        self.display_game()

    def display_game(self):
        x_text = self.display.width / 2
        y_text = self.display.height / 2 - 50
        font_size = 100
        text = 'Game Screen'
        self.helper.display_text(self.display.surface, text, font_size,
                                 (x_text, y_text))

        y_text = y_text + font_size
        font_size = 50
        text = 'Press O for game over screen'
        self.helper.display_text(self.display.surface, text, font_size,
                                 (x_text, y_text))
