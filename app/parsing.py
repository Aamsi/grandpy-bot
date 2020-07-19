import re


from app import stop_words


class ParsingMessage():
    """
        Parse the message sent by the user
    """

    def __init__(self, msg_received):
        self.stop_words = stop_words.STOP_WORDS
        self.msg_parsed = self.parse(msg_received)

    def parse(self, msg):
        delimiters = ['-', ' ', "'", '.', "?", "!"]
        reg_pattern = '|'.join(map(re.escape, delimiters))
        msg_splitted = re.split(reg_pattern, msg)
        msg_parsed = []

        # Get rid of stop words
        for word in msg_splitted:
            if word.lower() not in self.stop_words:
                msg_parsed.append(word)

        # If 'adresse' is in the message, we take the word just after"
        for i, word in enumerate(msg_parsed):
            if word == "adresse":
                return msg_parsed[i + 1]

        msg_parsed = ' '.join(msg_parsed)
        return msg_parsed
