import pygame


class GameController:

    def __init__(self) -> None:
        pass

    def handle_game_events(self, event):
        if event.type != pygame.KEYDOWN:
            return
        if event.key in [pygame.K_a, pygame.K_LEFT]:
            self.character.move_left()
        elif event.key in [pygame.K_d, pygame.K_RIGHT]:
            self.character.move_right()

