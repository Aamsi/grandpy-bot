import requests

from app import app_bot, parsing, settings


class MapInfo():

    def __init__(self, msg_received):
        self.msg_received = msg_received
        self.parse = parsing.ParsingMessage(self.msg_received)
        self.msg_parsed = self.parse.keyword 
        self.api_key = settings.GOOGLE_API_KEY
        self.url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
    
    def get_address_and_coord(self):
        payloads = {
            'input': self.msg_parsed,
            'inputtype': 'textquery',
            'fields': 'formatted_address,geometry',
            'key': self.api_key,
        }
        r = requests.get(self.url, payloads)
        print(r.json())
        print(r.url)
        if r.json()['status'] == "ZERO_RESULTS":
            return None
        else:
            formatted_address = r.json()['candidates'][0]['formatted_address']
            geometry = (r.json()['candidates'][0]['geometry']['location']['lat'],
                        r.json()['candidates'][0]['geometry']['location']['lng'])
            return {
                'formatted_address': formatted_address,
                'geometry': geometry
            }
        

