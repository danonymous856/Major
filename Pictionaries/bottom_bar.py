import pygame
from button import Button, TextButton

class BottomBar:
    COLORS = {
        0: (255,255,255),
        1: (0, 0, 0),
        2: (255, 0, 0),
        3: (0, 255, 0),
        4: (0, 0, 255),
        5: (255, 255, 0),
        6: (255, 140, 0),
        7: (165, 42, 42),
        8: (128, 0, 128),
    }

    def __init__(self,x,y,game):
        self.x = x
        self.y = y
        self.WIDTH = 720
        self.HEIGHT = 100
        self.BORDER_THICKNESS = 5
        self.game = game
        self.clear_button = TextButton(self.x + self.y)
