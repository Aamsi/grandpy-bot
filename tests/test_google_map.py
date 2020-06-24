import unittest
import requests_mock
import requests

# MARCHE PAAAAAAAAAAAS
from app.google_map import MapInfo


class MapInfoTest(unittest.TestCase):
    RESULT = {'candidates': 
                [{'formatted_address': '7 Cité Paradis, 75010 Paris, France',
                'geometry': {
                    'location': 
                            {'lat': 48.8748465, 
                            'lng': 2.3504873}}}],
                'status': 'OK'}

    def test_google_url(self):
        # Mettre l'API key de settings
        url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=OpenClassrooms&inputtype=textquery&fields=formatted_address%2Cgeometry&key=12345"
        map_info = MapInfo("OpenClassrooms")
        expected_formatted_address = self.RESULT['candidates'][0]['formatted_address']
        expected_geometry = (self.RESULT['candidates'][0]['geometry']['location']['lat'],
                            self.RESULT['candidates'][0]['geometry']['location']['lng'])
        expected_result = {
            'formatted_address': expected_formatted_address,
            'geometry': expected_geometry
        }

        with requests_mock.Mocker() as m:
            m.get(url, json=self.RESULT)
            result_to_test = map_info.get_address_and_coord()

        self.assertEqual(result_to_test, expected_result)




if __name__ == '__main__':
    unittest.main()