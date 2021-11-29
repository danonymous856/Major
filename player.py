# My first major project

class Player(object):
    def __init__(self,name,ipp):
        self.ipp=ipp
        self.name=name
        self.score=0

    def update_score(self,a):
        self.score+=a

    def guess(self,string):
        pass

    def disconnect(self):
        pass

    def get_score(self):
        return self.score

    def get_name(self):
        return self.name

    def get_score(self):
        return self.score