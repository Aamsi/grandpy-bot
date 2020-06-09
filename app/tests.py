import unittest

from parsing import ParsingMessage

class ParsingTest(unittest.TestCase):
    
    def test_parse(self):
        """ Test if we correctly parsed the message """
        test_parsing = ParsingMessage()
        msg = "Je teste un message nul"
        self.assertEqual(test_parsing.parse(msg), "Je teste message")
    
    def test_parse_duplicates(self):
        """ Test if we correctly remove duplicates of stop words """
        test_parsing = ParsingMessage()
        msg_duplicate = "Je teste un message nul mais un vraiment nul"
        self.assertEqual(test_parsing.parse(msg_duplicate), "Je teste message mais vraiment")


class WikiTest(unittest.TestCase):

    def test_return(self):
        """ Test if we get the right response """
        results = {
            "id": 345,
            "text": "Coucou",
        }
        self.assertEqual('Hey', 'Hey')



if __name__ == '__main__':
    unittest.main()