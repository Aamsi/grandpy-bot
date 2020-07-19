import unittest
import requests_mock

from flask import Flask
from requests import Request

from app.routes import process_message
from app.settings import GOOGLE_API_KEY
from app import app_bot


class ProcessTest(unittest.TestCase):
    RESULT_NO_PLACE = {'response': 'fail', "error": "placerror"}
    RESULT_NO_SUMMARY = {'response': 'fail', 'error': 'no address and summary'}
    RESULT_PLACE = {
        'candidates': [{
            'formatted_address': '7 Cité Paradis, 75010 Paris, France',
            'geometry': {
                'location': {
                    'lat': 48.8748465,
                    'lng': 2.3504873
                }
            }
        }],
        'status': 'OK'
    }

    def test_process_msg_no_place(self):
        """ Test view if no place is found with google map """
        with app_bot.test_client() as c:
            response = c.post("process_msg", data={"msg_content": "ffff"})
            self.assertEqual(response.get_json(), self.RESULT_NO_PLACE)
    
    def test_process_msg_no_summary(self):
        """ Test view if place is found but no summary found with wikipedia """
        with app_bot.test_client() as c:
            url_place = "https://maps.googleapis.com/maps/api/place/\
findplacefromtext/json"
            place_payloads = {
                'input': "Openclassrooms",
                'inputtype': 'textquery',
                'fields': 'formatted_address,geometry',
                'key': GOOGLE_API_KEY,
            }
            url_place_prepare = Request('GET', url_place, params=place_payloads).prepare()

            url_wiki_get_pages = "https://fr.wikipedia.org/w/api.php"
            get_pages_payload = {
                'action': 'query',
                'format': 'json',
                'list': 'geosearch',
                'gscoord': "48.8748465|2.3504873"
            }
            url_wiki_get_pages_prepare = Request('GET', url_wiki_get_pages, params=get_pages_payload).prepare()
            url_wiki_result_pages = "https://fr.wikipedia.org/api/rest_v1/page/summary/Cite_Paradis"

            with requests_mock.Mocker() as m:
                m.get(url_place_prepare.url, json=self.RESULT_PLACE)
                m.get(url_wiki_get_pages_prepare.url, json={
                    'query': {
                        'geosearch': [{'title': 'Cite_Paradis'}]
                    }
                })
                m.get(url_wiki_result_pages, json={'extract': None})
                response = c.post("process_msg", data={"msg_content": "OpenClassrooms"})
                self.assertEqual(response.get_json(), self.RESULT_NO_SUMMARY)

            






# faire instance de l'app
# flask --> test client
#  app,test_client
# Chercher sur google comment chercher dans une zone