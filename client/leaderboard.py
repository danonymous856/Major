"""
return : Represents The leaderboard object for the client side of the game.
"""

import pygame

from client import player


class Leaderboard(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.WIDTH = 200
        self.HEIGHT_ENTRY = 80
        self.players = []
        self.name_font = pygame.font.SysFont("comicsans",25,bold = True)
        self.score_font = pygame.font.SysFont("comicsans",20)
        self.rank_font = pygame.font.SysFont("comicsans",60)
        self.BORDER_THICKNESS = 5

    def draw(self,win):
        score = [(player.name, player.score) for player in self.players]
        score.sort(key=lambda x: x[1],reverse=True)