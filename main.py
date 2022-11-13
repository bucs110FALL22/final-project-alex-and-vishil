import pygame
from src.controller import Controller


def main():
	pygame.init()
	surface = pygame.display.set_mode((1200, 1000))
	controller = Controller()
	controller.mainloop()


# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
	main()
