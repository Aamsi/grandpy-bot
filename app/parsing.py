import re


from app import app_bot, stop_words


class ParsingMessage():
    
    def __init__(self, msg_received):
        self.stop_words = stop_words.STOP_WORDS
        self.msg_parsed = self.parse(msg_received)
        self.keyword = self.get_keyword()

    def parse(self, msg):
        delimiters = ['-', ' ', "'", '.', "?", "!"]
        reg_pattern = '|'.join(map(re.escape, delimiters))
        msg_splitted = re.split(reg_pattern, msg)
        msg_parsed = []

        for word in msg_splitted:
            if word.lower() not in self.stop_words:
                msg_parsed.append(word)

        return msg_parsed
    
    def get_keyword(self):
        if 'adresse' in self.msg_parsed:
            index = self.msg_parsed.index('adresse')
            return self.msg_parsed[index + 1]
        
        return None
