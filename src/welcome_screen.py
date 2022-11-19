from src.display import Display
from src.helper import Helper
from src.assets import Assets
from src.image import Image


class WelcomeScreen:

    def __init__(self, display: Display) -> None:
        self.display = display
        self.init_welcome_charater_image()

    def init_welcome_charater_image(self):
        image_file = Assets.images.get('welcome-character')
        image_width = self.display.width / 4
        image_height = self.display.height / 4
        self.welcome_image = Image(image_file, image_width, image_height)

    def draw(self):
        self.draw_game_title()
        self.draw_welcome_character()
        self.diplay_instructions()

    def draw_game_title(self):
        surface = self.display.surface
        x_text = self.display.width / 2
        y_text = self.display.height / 2

        text = 'Mario Bomber'
        font_size = 100
        Helper.print(surface, text, font_size, (x_text, y_text))

        y_text += font_size
        text = 'Press SPACE to start'
        font_size = 50
        Helper.print(surface, text, font_size, (x_text, y_text))

        y_text += 2 * font_size
        text = 'By Alex E. and Vishil P.'
        font_size = 30
        Helper.print(surface, text, font_size, (x_text, y_text))

    def diplay_instructions(self):
        surface = self.display.surface
        x_text = self.display.width / 2
        y_text = self.display.height - 120

        text = 'Instructions: Bombs kill you and mushrooms keep you alive!'
        font_size = 20
        Helper.print(surface, text, font_size, (x_text, y_text))

        y_text += font_size
        text = 'Every bomb gives you points. Turtles slow the game down'
        font_size = 20
        Helper.print(surface, text, font_size, (x_text, y_text))

        y_text += font_size
        text = 'Press G for Grid (debug). S to toggle music. Q to Quit'
        font_size = 20
        Helper.print(surface, text, font_size, (x_text, y_text))

    def draw_welcome_character(self):
        surface = self.display.surface
        x_image = self.display.width / 4
        y_image = self.display.height / 4
        self.welcome_image.draw(surface, x_image, y_image)
