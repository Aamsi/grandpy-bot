import unittest

from app.wiki import WikiInfo


class WikiTest(unittest.TestCase):
    RESULT = 'La cité Paradis est une voie publique située dans le 10e\xa0arrondissement de Paris.'

    def test_return(self):
        """ Test if we get the right response """
        coord = ('48.87409', '2.35064')
        wiki = WikiInfo(coord[0], coord[1])
        summary = wiki.get_summary()
        self.assertEqual(summary, self.RESULT)


if __name__ == '__main__':
    unittest.main()