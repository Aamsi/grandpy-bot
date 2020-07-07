import unittest
import requests_mock

from requests import Request

from app.google_map import MapInfo
from app.settings import GOOGLE_API_KEY


class MapInfoTest(unittest.TestCase):
    RESULT_OK = {
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

    RESULT_KO = {'status': 'ZERO_RESULTS'}

    def __init__(self, *args, **kwargs):
        super(MapInfoTest, self).__init__(*args, **kwargs)
        self.url = "https://maps.googleapis.com/maps/api/place/\
findplacefromtext/json"
        self.payloads = {
            'input': "Openclassrooms",
            'inputtype': 'textquery',
            'fields': 'formatted_address,geometry',
            'key': GOOGLE_API_KEY,
        }

    def test_google_url_ok(self):
        url_prepare = Request('GET', self.url, params=self.payloads).prepare()
        result = self.RESULT_OK['candidates'][0]
        expected_formatted_address = result['formatted_address']
        expected_geometry = (result['geometry']['location']['lat'],
                             result['geometry']['location']['lng'])
        expected_result = {
            'address': expected_formatted_address,
            'geometry': expected_geometry
        }

        map_info = MapInfo("Openclassrooms")
        with requests_mock.Mocker() as m:
            m.get(url_prepare.url, json=self.RESULT_OK)
            result_to_test = map_info.get_address_and_coord()

        self.assertEqual(result_to_test, expected_result)

    def test_google_url_ko(self):
        url_prepare = Request('GET', self.url, params=self.payloads).prepare()
        expected_result = None

        map_info = MapInfo("Openclassrooms")
        with requests_mock.Mocker() as m:
            m.get(url_prepare.url, json=self.RESULT_KO)
            result_to_test = map_info.get_address_and_coord()

        self.assertEqual(result_to_test, expected_result)

    def test_error_http(self):
        url_prepare = Request('GET', self.url, params=self.payloads).prepare()
        expected_result = None

        map_info = MapInfo("Openclassrooms")
        with requests_mock.Mocker() as m:
            m.get(url_prepare.url, json=self.RESULT_KO, status_code=404)
            result_to_test = map_info.get_address_and_coord()

        self.assertEqual(result_to_test, expected_result)
