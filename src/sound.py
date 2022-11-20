import pygame


class Sound:
    '''
    Wrapper around pygame to easily work with sounds
    '''

    def __init__(self, file_name: str) -> None:
        '''
        constructor
        file_name: (str) file containing the sound
        '''
        self.file_name = file_name
        self.sound = pygame.mixer.Sound(self.file_name)

    def beep(self):
        '''
        beeps, that is plays the sound once
        '''
        pygame.mixer.Sound.play(self.sound)
        pygame.mixer.music.stop()

    def play(self):
        '''
        Plays the sound continously until stop() is called
        '''
        pygame.mixer.Sound.play(self.sound)

    def stop(self):
        '''
        Stops playing the sound continously
        '''
        pygame.mixer.Sound.stop(self.sound)
