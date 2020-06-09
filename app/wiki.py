import requests

from parsing import ParsingMessage


# title = ""
# payload = {
#     'action': 'query',
#     'format': 'json',
#     'generator': 'search',
#     'gsrsearch': 'Openclassroom',
# }

# r = requests.get("https://fr.wikipedia.org/w/api.php", params=payload)
# print(r.url)
# for page in r.json()['query']['pages'].values():
#     if page['title'] == "OpenClassrooms":
#         title = page['title']

# payload = {
#     'action': 'query',
#     'format': 'json',
#     'pageids': 4338589,
# }

# r = requests.get(f"https://fr.wikipedia.org/api/rest_v1/page/summary/{title}")
# print(r.json()['extract'])

class WikiInfo():

    def __init__(self, msg_received):
        self.msg_received = msg_received
        self.parse = ParsingMessage(self.msg_received)
        self.get_title_payload = {
            'action': 'query',
            'format': 'json',
            'generator': 'search',
            'gsrsearch': self.parse.keyword,
        }
        self.get_title_url = "https://fr.wikipedia.org/w/api.php"
        self.title = self.get_title()
        self.get_summary_url = f"https://fr.wikipedia.org/api/rest_v1/page/summary/{self.title}"

    def get_title(self):
        msg = self.parse.keyword
        r = requests.get(self.get_title_url, params=self.get_title_payload)
        for page in r.json()['query']['pages'].values():
            if msg in page['title'].split(' '):
                return page['title']

    def get_summary(self):
        if self.title:
            r = requests.get(self.get_summary_url)
            summary = r.json()['extract']
            return summary

        return None

# wiki = WikiInfo("Je veux l'adresse d'OpenClassrooms")
# summary = wiki.get_summary()
# print(summary)