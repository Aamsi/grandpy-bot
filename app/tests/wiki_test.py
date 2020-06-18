import unittest

from app.wiki import WikiInfo


class WikiTest(unittest.TestCase):

    def test_return(self):
        """ Test if we get the right response """
        wiki = WikiInfo("Je veux l'adresse d'OpenClassrooms")
        msg = "OpenClassrooms"
        result = "OpenClassrooms est un site web de formation en ligne qui \
propose à ses membres des cours certifiants et des parcours \
débouchant sur des métiers en croissance. Ses contenus sont \
réalisés en interne, par des écoles, des universités, \
des entreprises partenaires comme Microsoft ou IBM, ou \
historiquement par des bénévoles. Jusqu'en 2018, n'importe \
quel membre du site pouvait être auteur, via un outil nommé \
« interface de rédaction » puis « Course Lab ». De nombreux \
cours sont issus de la communauté, mais ne sont plus mis en \
avant. Initialement orientée autour de la programmation \
informatique, la plate-forme couvre depuis 2013 des \
thématiques plus larges tels que le marketing, \
l'entrepreneuriat et les sciences."
        summary = wiki.get_summary()
        self.assertEqual(summary, result)


if __name__ == '__main__':
    unittest.main()