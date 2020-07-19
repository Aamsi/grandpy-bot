import unittest

from app.parsing import ParsingMessage


class ParsingTest(unittest.TestCase):

    def test_parse_address(self):
        """
            Test if we correctly parsed the message with 'adresse' in message
        """
        msg = "Je veux l'adresse d'OpenClassrooms"
        test_parse = ParsingMessage(msg)
        self.assertEqual(test_parse.msg_parsed, "OpenClassrooms")

    def test_parse_no_address(self):
        """
           Test if we correctly parsed the message without 'address' in message
        """
        msg = "C'est ou OpenClassrooms"
        test_parse = ParsingMessage(msg)
        self.assertEqual(test_parse.msg_parsed, "OpenClassrooms")
