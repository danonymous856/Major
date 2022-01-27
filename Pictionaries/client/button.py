"""
Stores interface for button and the two concreate button classes to be used in the UI .
"""

import pygame

class Button:
    def __init__(self,x,y,width,height,color,border_color = (0,0,0)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, win):
        pygame.draw.rect(win, self.border_color, (self.x, self.y, self.width, self.height), 0)
        pygame.draw.rect(win, self.color, (
            self.x + self.BORDER_WIDTH, self.y + self.BORDER_WIDTH, self.width - self.BORDER_WIDTH * 2,
            self.height - self.BORDER_WIDTH * 2), 0)