import pygame
from config import *

class MainGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((RESOLUTION_X, RESOLUTION_Y))
        pygame.display.set_caption("Business Simulator")
    def quit(self):
    def checkEvents(self):
    def run(self):
        while True:
            for event in self.checkEvents():
                if event.type == pygame.QUIT:
                    self.quit()
                self.render()
    def render(self):
