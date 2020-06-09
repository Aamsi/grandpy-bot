import re

from stop_words import STOP_WORDS


class ParsingMessage():
    
    def __init__(self):
        self.stop_words = STOP_WORDS
        self.msg = ""
    
    def parse(self, msg):
        delimiters = ['-', ' ', "'", '.', "?", "!"]
        reg_pattern = '|'.join(map(re.escape, delimiters))
        msg_splitted = re.split(reg_pattern, msg)
        msg_parsed = []
        print(msg_splitted)
        for word in msg_splitted:
            if word.lower() not in self.stop_words:
                msg_parsed.append(word)
        self.msg = ' '.join(msg_parsed)
        




parsing = ParsingMessage()
parsing.parse("Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?")

print(parsing.msg)