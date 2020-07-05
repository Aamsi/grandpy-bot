import unittest

from app.parsing import ParsingMessage


class ParsingTest(unittest.TestCase):
    
    def test_parse(self):
        """ Test if we correctly parsed the message """
        msg = "Je veux l'adresse d'OpenClassrooms"
        test_parsing = ParsingMessage(msg)
        self.assertEqual(test_parsing.msg_parsed, 'veux adresse OpenClassrooms')
