"""
Top bar displaying information abt the Round
"""
import pygame

class TopBar(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.word = " "
        self.round = 1
        self.max_round = 8
        self.round_font = pygame.font.SysFont("comicsans",50)
        self.time = 75
        self.drawing = False

    def draw(self,win):
        pygame.draw.rect(win,(0,0,0),(self.x,self.y,self.width,self.height),self.BORDER_THICKNESS)

        txt = self.round_font.render(f"Round {self.round} of  {self.max_round}",1,(0,0,0))
        win.blit(txt,(self.x + 10,self.y + self.height/2 - txt.get_height()/2))

        if self.drawing:
            wrd = self.word
        else:
            wrd = TopBar.underscore_text(self.word)
        txt = self.round_font.render(wrd,1,(0,0,0))
        win.blit(txt,(self.x + self.width/2 - txt.get_width()/2,self.y + self.height/2 - txt.get_height()/2+10))
