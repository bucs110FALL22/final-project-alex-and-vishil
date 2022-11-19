from src.bomb import Bomb
from src.scoreboard import Scoreboard
from src.image import Image
from src.display import Display
from src.helper import Helper
from src.game_model import GameModel
from src.assets import Assets


class GameScreen:
    '''
    GameScreen is the view object for the game.
    '''

    def __init__(self, display: Display, game_model: GameModel) -> None:
        '''
        constructor
        display: (Display) object containing the display information.
        game_model: (GameModel) model/data/state of the game
        '''
        self.helper = Helper()
        self.display = display
        self.game_model = game_model
        self.scoreboard = Scoreboard(display, game_model)
        self.init_character_image()
        self.init_bomb_image()

    def draw(self):
        '''
        Draws the game view.
        '''
        self.draw_scoreboard()
        self.draw_character()
        self.draw_bombs()

    def init_character_image(self):
        '''
        Initializes the character image
        '''
        width = self.display.lane_width
        height = self.display.lane_width
        image_file = Assets.images.get('character')
        self.character_image = Image(image_file, width, height)

    def init_bomb_image(self):
        '''
        Initializes the bombs image
        '''
        width = self.display.lane_width
        height = self.display.lane_width
        image_file = Assets.images.get('bomb')
        self.bomb_image = Image(image_file, width, height)

    def draw_character(self):
        '''
        Draws the character on the screen.
        '''
        x_character = self.display.lane_width * self.game_model.character.lane
        y_character = self.display.height * (
            100 - self.game_model.character.height) / 100
        self.character_image.draw(self.display.surface, x_character,
                                  y_character)

    def draw_bombs(self):
        '''
        Draws all the bombs on the screen.
        '''
        for bomb in self.game_model.bombs:
            self.draw_bomb(bomb)

    def draw_bomb(self, bomb: Bomb):
        '''
        Draws a bomb on the screen.
        bomb: (Bomb) bomb to draw.
        '''
        if bomb.is_state_active():
            self.draw_bomb_unexploted(bomb)
            return

        if bomb.is_state_evaded():
            self.draw_bomb_value(bomb)
            return

        if bomb.is_state_target_hit():
            self.draw_bomb_exploded(bomb)
            return

    def draw_bomb_unexploted(self, bomb):
        '''
        Draws a bomb in an unexploted state.
        bomb: (Bomb) bomb to draw.
        '''
        surface = self.display.surface
        x_bomb, y_bomb = self.get_bomb_screen_pos(bomb)
        self.bomb_image.draw(surface, x_bomb, y_bomb)

    def draw_bomb_value(self, bomb):
        '''
        Draws the bomb in exploded state. We currently display the score value of the item.
        bomb: (Bomb) bomb to draw.
        '''
        surface = self.display.surface
        x_bomb, y_bomb = self.get_bomb_screen_pos(bomb)
        x_text = x_bomb + self.display.lane_width / 2
        y_text = y_bomb
        text = str(bomb.score_value)
        font_size = 40
        Helper.print(surface, text, font_size, (x_text, y_text))

    def draw_bomb_exploded(self, bomb):
        '''
        Draws the bomb in exploded state. We currently display the score value of the item.
        bomb: (Bomb) bomb to draw.
        '''
        surface = self.display.surface
        x_bomb, y_bomb = self.get_bomb_screen_pos(bomb)
        x_text = x_bomb + self.display.lane_width / 2
        y_text = y_bomb
        text = 'BOOM!'
        font_size = 40
        Helper.print(surface, text, font_size, (x_text, y_text))

    def get_bomb_screen_pos(self, bomb):
        '''
        Calculates the screen position of the bomb by translating the logical units to pixels.
        bomb: (Bomb) bomb to draw.
        return: (tuple) Bomb coordinates in pixels
        '''
        x_bomb = bomb.lane * self.display.lane_width
        y_bomb = bomb.log_depth * self.display.height / 100
        return x_bomb, y_bomb

    def draw_scoreboard(self):
        '''
        Draws the scoreboard
        '''
        self.scoreboard.draw()
