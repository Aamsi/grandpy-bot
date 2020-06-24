import requests


from app import app_bot


class WikiInfo():

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
        self.get_title_url = "https://fr.wikipedia.org/w/api.php"
        self.title = self.get_title()
        self.get_summary_url = f"https://fr.wikipedia.org/api/rest_v1/page/summary/{self.title}"

    def get_title(self):
        get_title_payload = {
            'action': 'query',
            'format': 'json',
            'list': 'geosearch',
            'gscoord': f"{self.latitude}|{self.longitude}"
        }
        r = requests.get(self.get_title_url, params=get_title_payload)

        return r.json()['query']['geosearch'][0]['title']

    def get_summary(self):
        if self.title:
            r = requests.get(self.get_summary_url)
            print(r.url)
            summary = r.json()['extract']
            return summary

        return None

# map_info = WikiInfo('48.87409', '2.35064')
# summary = map_info.get_summary()
# print(summary)

# je dois specifier que je veux situation et acces? C'est debile pcq c'est pas generique et que ca fonctionne que pour tres peu de page.
# Je prefere utiliser extract car ca marche pour toutes les pages
# https://fr.wikipedia.org/w/api.php?action=parse&pageid=5653202&format=json&prop=wikitext&section=1