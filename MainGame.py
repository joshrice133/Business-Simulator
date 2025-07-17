import sys
import pygame
from config import *

class MainGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((RESOLUTION_X, RESOLUTION_Y))
        pygame.display.set_caption("Business Simulator")

    def quit(self):
        pygame.quit()
        sys.exit()

    def checkEvents(self):
        return pygame.event.get()

    def render(self):
        self.screen.fill((0, 0, 0))
        pygame.display.flip()

    def run(self):
        while True:
            for event in self.checkEvents():
                if event.type == pygame.QUIT:
                    self.quit()
                self.render()

if __name__ == "__main__":
    MainGame().run()
