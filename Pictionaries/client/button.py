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

    def click(self, x, y):
        """
        if user clicked on button
        :param x: float
        :param y: float
        :return: bool
        """

        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True  # user clicked button

        return False

class TextButton(Button):
    def __init__(self,x,y,width,height,color,text,border_color = (0,0,0)):
        super().__init__(x,y,width,height,color,border_color)
        self.text = text
        self.text_font = pygame.font.Sysfont("comicsans",30)
