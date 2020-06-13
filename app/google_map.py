import requests

from parsing import ParsingMessage


class MapInfo():

    def __init__(self, msg_received):
        self.parse = ParsingMessage("Je veux l'adresse d'OpenClassrooms")
        self.msg_received = self.parse.keyword 
        self.api_key = ""
        self.url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
    
    def get_coordinates(self):
        payloads = {
            'input': self.msg_received,
            'inputtype': 'textquery',
            'fields': 'geometry',
            'key': self.api_key,
        }
        r = requests.get(self.url, payloads)
        print(r.url)
        geometry = (r.json()['candidates'][0]['geometry']['location']['lat'],
                    r.json()['candidates'][0]['geometry']['location']['lng'])
        
        return geometry

# mape = MapInfo("OpenClassrooms")
# mape.get_coordinates()