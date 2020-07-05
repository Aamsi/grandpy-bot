import unittest
import requests_mock
import json

from requests import Request

from app.wiki import WikiInfo


class WikiTest(unittest.TestCase):
    RESULT = {
        'extract': 'La cité Paradis est une voie publique située dans le 10e\xa0arrondissement de Paris.'
    }

    def __init__(self, *args, **kwargs):
        super(WikiTest, self).__init__(*args, **kwargs)
        self.get_pages_url = "https://fr.wikipedia.org/w/api.php"
        self.get_pages_payload = {
            'action': 'query',
            'format': 'json',
            'list': 'geosearch',
            'gscoord': "48.87409|2.35064"
        }

    def test_get_response(self):
        """ Test if we get the right response """
        address = "7 Cité Paradis, 75010 Paris, France"
        url_with_params = Request('GET', 
                                  self.get_pages_url,
                                  params=self.get_pages_payload).prepare()
        with open("/home/aamsi/Documents/OC/P7/tests/pages_wiki.json") as json_file:
            expected_result = json.load(json_file)

        wiki = WikiInfo(address, '48.87409', '2.35064')
        with requests_mock.Mocker() as m:
            m.get(url_with_params.url, json=expected_result)
            result_to_test = wiki.get_response()

        self.assertEqual(result_to_test, expected_result)
    
    def test_get_matching_page(self):
        address = "7 Cité Paradis, 75010 Paris, France"
        url_with_params = Request('GET', 
                                  self.get_pages_url,
                                  params=self.get_pages_payload).prepare()
        expected_result = "Cit\u00e9 Paradis"
        with open("/home/aamsi/Documents/OC/P7/tests/pages_wiki.json") as json_file:
            response = json.load(json_file)
        
        wiki = WikiInfo(address, '48.87409', '2.35064')
        result_to_test = wiki.get_matching_page(response)

        self.assertEqual(result_to_test, expected_result)
    
    def test_get_matching_page_first(self):
        # Pour avoir la page correspondante, on utilise l'addresse, mais si y a 0 resultat, on prend la premiere page
        address = "Champ de Mars, 5 Avenue Anatole France, 75007 Paris"
        url_with_params = Request('GET', 
                                  self.get_pages_url,
                                  params=self.get_pages_payload).prepare()
        expected_result = "Hôtel Botterel de Quintin"
        with open("/home/aamsi/Documents/OC/P7/tests/pages_wiki.json") as json_file:
            response = json.load(json_file)

        wiki = WikiInfo(address, '48.858370', '2.294481')
        result_to_test = wiki.get_matching_page(response)

        self.assertEqual(result_to_test, expected_result)
    
    def test_get_summary_if_page(self):
        address = "7 Cité Paradis, 75010 Paris, France"
        page = "Cité_Paradis"
        url = f"https://fr.wikipedia.org/api/rest_v1/page/summary/{page}"
        print(url)
        expected_result = self.RESULT['extract']

        wiki = WikiInfo(address, '48.87409', '2.35064')
        with requests_mock.Mocker() as m:
            m.get(url, json=self.RESULT)
            result_to_test = wiki.get_summary("Cité_Paradis")
        
        self.assertEqual(result_to_test, expected_result)
