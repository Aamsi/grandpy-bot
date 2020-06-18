import unittest

from app.parsing import ParsingMessage


class ParsingTest(unittest.TestCase):
    
    def test_parse(self):
        """ Test if we correctly parsed the message """
        msg = "Je veux l'adresse d'OpenClassrooms"
        test_parsing = ParsingMessage(msg)
        self.assertEqual(test_parsing.keyword, "OpenClassrooms")
    
    def test_parse_duplicates(self):
        """ Test if we correctly remove duplicates of stop words """
        msg_duplicate = "Je veux l'adresse d'OpenClassrooms veux"
        test_parsing = ParsingMessage(msg_duplicate)
        self.assertEqual(test_parsing.keyword, "OpenClassrooms")




if __name__ == '__main__':
    unittest.main()
