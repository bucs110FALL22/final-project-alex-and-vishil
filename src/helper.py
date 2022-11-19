import pygame


class Helper:

    def text_objects(text, font):
        textSurface = font.render(text, True, 'white')
        return textSurface, textSurface.get_rect()

    def print(surface, text, size, center):
        largeText = pygame.font.Font('freesansbold.ttf', size)
        TextSurf, TextRect = Helper.text_objects(text, largeText)
        TextRect.center = center
        surface.blit(TextSurf, TextRect)
