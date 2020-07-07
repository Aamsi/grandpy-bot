import requests

from app import settings


class MapInfo():

    def __init__(self, msg_parsed):
        self.msg_parsed = msg_parsed
        self.api_key = settings.GOOGLE_API_KEY
        self.url = "https://maps.googleapis.com/maps/api/place/\
findplacefromtext/json"

    def get_address_and_coord(self):
        payloads = {
            'input': self.msg_parsed,
            'inputtype': 'textquery',
            'fields': 'formatted_address,geometry',
            'key': self.api_key,
        }
        r = requests.get(self.url, payloads)
        print(r.url)
        if not r.ok:
            return None
        try:
            res = r.json()
            if res['status'] == "OK":
                formatted_address = res['candidates'][0]['formatted_address']
                location = res['candidates'][0]['geometry']['location']
                geometry = (location['lat'],
                            location['lng'])
                return {
                    'address': formatted_address,
                    'geometry': geometry
                }
            else:
                return None
        except KeyError:
            return None
