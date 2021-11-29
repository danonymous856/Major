class ROund(object):
    def __init__(self,word,player_drawing):
        self.word=word
        self.player_drawing=player_drawing
        self.player_guessed=[]
        self.skips=0
        self.player_scores = {player:0 for player in player}
        self.time=0

    def guess(self,player,wrd):
        """
        :returns bool if player got guess right
        :param player:player
        :param wrd:str
        :return bool
        """
        return wrd==self.word