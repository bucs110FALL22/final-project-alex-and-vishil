from src.game_screen import GameScreen
from src.game_controller import GameController
from src.display import Display
from src.game_model import GameModel


class Game:

    def __init__(self, display: Display) -> None:
        self.game_model = GameModel()
        self.game_controller = GameController(self.game_model)
        self.game_screen = GameScreen(display, self.game_model)

    def start(self):
        self.game_model.start_game()

    def hangle_event(self, events):
        self.game_controller.handle_game_events(events)

    def update_data(self):
        return self.game_model.update_data()

    def draw(self):
        self.game_screen.draw()

    def is_over(self) -> bool:
        return self.game_model.is_over
