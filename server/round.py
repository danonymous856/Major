"""
Represent a round of the game , storing things like
word,time,skips,drawing player and more.
"""

import time as t
from _thread import *
from .chat import Chat

class Round(object):
    def __init__(self,word,player_drawing,player):
        """
        init object
        :param word:word
        :param player_drawing:player
        :param player:player[]
        """
        self.word=word
        self.player_drawing=player_drawing
        self.player_guessed=[]
        self.skips=0
        self.player_scores = {player:0 for player in player}
        self.time=75
        self.chat = Chat(self)
        self.game = game
        start_new_thread(self.time_thread, ())

    def skip(self):
        """
        :returns True if round skipped threshold met
        :return: boolean
        """

        self.skips +=1
        if self.skips > len(self.game.players) - 2:
            return  True

        return False

    def get_scores(self):
        """
        Returns all the players scores
        :return:
        """
        return self.player_scores

    def get_score(self):
        """
        Returns the score of a speciic Player
        :return:
        """

        if player in self.player_scores:
            return self.player_scores[player]
        else:
            raise Exception("Player is not in score list")

    def time_thread(self):
        """
        runs in thread to keep track of time
        :return: None
        """
        while self.time > 0:
            t.sleep(1)
            self.time -= 1
        self.end_round("Time is up")

    def guess(self,player,wrd):
        """
        :returns bool if player got guess right
        :param player:player
        :param wrd:str
        :return bool
        """
        correct = wrd ==self.word
        if correct:
            self.player_guessed.append(player)
            self.chat.update_chat(f"{player.name} has guessed the word. ")
            return True


        self.chat.update_chat(f"{player.name} guessed {wrd}")
        return False

    def player_left(self,player):
        """
        :param player:player
        :return: None
        """
        if player in self.player_scores:
            del self.player_scores[player]

        if player in self.player_guessed:
            self.player_guessed.remove(player)

        if player == self.player_drawing:
            self.end_round("Drawing player leaves")

    def end_round(self,msg):
        # TODO implement end_round functionality
        for player in self.game.players:
            if player in self.player_scores:
                player.update_score(self.player_scores[player])
        self.game.round_ended()