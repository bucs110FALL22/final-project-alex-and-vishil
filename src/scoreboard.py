from src.helper import Helper
from src.image import Image
from src.assets import Assets
from src.display import Display


class Scoreboard():
    '''
    View for the scoreboard
    '''

    def __init__(self, display: Display) -> None:
        self.display = display
        self.init_health_image()

    def init_health_image(self):
        width = self.display.lane_width / 2
        height = self.display.lane_width / 2
        image_file = Assets.images.get('health')
        self.health_image = Image(image_file, width, height)

    def draw(self, health: int = 0, score: int = 0, max_score: int = 0):
        self.draw_health(health)
        self.draw_score(score)
        self.draw_max_score(max_score)

    def draw_health(self, health: int):
        margin = self.display.lane_width / 2
        for live in range(health):
            x_health = margin + margin * live
            y_health = margin / 2
            self.health_image.draw(self.display.surface, x_health, y_health)

    def draw_score(self, score: int):
        margin = self.display.lane_width / 2
        x_score = self.display.width / 2
        y_score = margin
        text_score = 'Score: ' + str(score)
        Helper.print(self.display.surface, text_score, 30, (x_score, y_score))

    def draw_max_score(self, max_score: int):
        margin = self.display.lane_width / 2
        x_score = self.display.width - 3 * margin
        y_score = margin
        text_score = 'Max: ' + str(max_score)
        Helper.print(self.display.surface, text_score, 30, (x_score, y_score))
