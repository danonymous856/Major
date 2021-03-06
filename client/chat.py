from round import ROund

class Chat(object):
    def __init__(self):
        self.content = []
        self.round = None

    def update_chat(self,msg):
        self.content.append(msg)

    def get_chat(self):
        return self.content

    def __len__(self):
        return len(self.content)

    def __str__(self):
        return "".join(self.content)

    def __repr__(self):
        return str(self)