"""
Represents the board object for the game.
"""
from curses import COLORS

import pygame
import random

class Board(object):
    ROWS = COLS = 90
    COLORS = {
        0: (255,255,255),
        1: (0,0,0),
        2: (255, 0,0),
        3: (0, 255, 0),
        4: (0, 0, 255),
        5: (255, 255, 0),
        6: (255, 140, 0),
        7: (255, 42, 42),
        8: (128, 0, 128)
    }

def __init__(self,x,y):
    self.x = x
    self.y = y
    self.WIDTH = 720
    self.HEIGHT = 720
    self.compressed_board = []
    self.board = self.create_board()
    self.BORDER_THICKNESS = 5

