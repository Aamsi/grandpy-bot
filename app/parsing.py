from stop_words import STOP_WORDS


class ParsingMessage():
    
    def __init__(self):
        self.stop_words = STOP_WORDS
    
    def parse(self, msg):
        msg_list = msg.split(' ')
        for word in msg_list:
            if word in self.stop_words:
                msg_list.remove(word)
        msg = ' '.join(msg_list)
        return msg




# parsing = ParsingMessage()
# msg = parsing.parse("Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?")
# print(msg)