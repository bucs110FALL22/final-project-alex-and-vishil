from src.display import Display
from src.helper import Helper


class GameoverScreen:

    def __init__(self, display: Display) -> None:
        self.display = display

    def draw(self):
        self.display_game_over()

    def display_game_over(self):
        surface = self.display.surface
        x_text = self.display.width / 2
        y_text = self.display.height / 2

        text = 'Game Over'
        font_size = 100
        Helper.print(surface, text, font_size, (x_text, y_text))

        y_text += font_size
        text = 'Press SPACE to start'
        font_size = 50
        Helper.print(surface, text, font_size, (x_text, y_text))

        y_text += font_size
        text = 'Q to quit'
        font_size = 50
        Helper.print(surface, text, font_size, (x_text, y_text))
