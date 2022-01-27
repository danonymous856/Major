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
        self.clear_button = TextButton(self.x + self.WIDTH - 150,self.y + 25,100,50, (128,128,128),"Clear")
        self.clear_button = TextButton(self.x + self.WIDTH - 300, self.y + 25, 100, 50, (128, 128, 128),"Eraser")
        self.color_buttons = [Button(self.x + 20,self.y + 5,30,30, self.COLORS[0]),
                              Button(self.x + 50, self.y + 5, 30, 30, self.COLORS[1]),
                              Button(self.x + 80, self.y + 5, 30, 30, self.COLORS[2]),
                              Button(self.x + 20, self.y + 35, 30, 30, self.COLORS[3]),
                              Button(self.x + 50, self.y + 35, 30, 30, self.COLORS[4]),
                              Button(self.x + 80, self.y + 35, 30, 30, self.COLORS[5]),
                              Button(self.x + 20, self.y + 65, 30, 30, self.COLORS[6]),
                              Button(self.x + 50, self.y + 65, 30, 30, self.COLORS[7]),
                              Button(self.x + 80, self.y + 65, 30, 30, self.COLORS[8])
                              ]

    def draw(self,win):
        pygame.draw.rect(win,(0,0,0),(self.x, self.y ,self.WIDTH, self.HEIGHT),self.BORDER_THICKNESS)
        self.clear_button.draw(win)
        self.eraser_button.draw(win)

        for btn in self.color_buttons:
            btn.draw(win)

    def button_events(self):
        """
        handle all the button press events here
        :return: None
        """




