from src.display import Display
from src.pygame_helpers import Helpers
from src.assets import Assets
from src.image import Image


class WelcomeScreen:

    def __init__(self, display: Display) -> None:
        self.helper = Helpers()
        self.display = display
        self.welcome_image = Image(Assets.images.get('welcome-character'),
                                   self.display.width / 4,
                                   self.display.height / 4)

    def draw(self):
        x_text = self.display.width / 2
        y_text = self.display.height / 2 + 80
        self.helper.display_text(self.display.surface, 'Mario Bomber', 100,
                                 (x_text, y_text))
        self.helper.display_text(self.display.surface, 'Press SPACE to start',
                                 50, (x_text, y_text + 100))
        self.helper.display_text(self.display.surface,
                                 'By Alex E. and Vishil P.', 30,
                                 (x_text, y_text + 170))
        self.draw_welcome_character()
        self.diplay_instructions()

    def diplay_instructions(self):
        x_text = self.display.width / 2
        self.helper.display_text(
            self.display.surface,
            'Instructions: Bombs kill you and mushrooms keep you alive!', 20,
            (x_text, self.display.height - 120))
        self.helper.display_text(
            self.display.surface,
            'Every bomb gives you points. Turtles slow the game down', 20,
            (x_text, self.display.height - 80))
        self.helper.display_text(
            self.display.surface,
            'Press G for Grid (debug). S to toggle music. Q to Quit', 20,
            (x_text, self.display.height - 40))

    def draw_welcome_character(self):
        self.welcome_image.draw(self.display.surface, self.display.width / 4,
                                self.display.height / 4)
