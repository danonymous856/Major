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