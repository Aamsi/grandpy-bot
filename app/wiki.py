import requests


class WikiInfo():
    """
        Get the summary of the related place.
    """
    def __init__(self, address, latitude, longitude):
        self.address = address
        self.latitude = latitude
        self.longitude = longitude
        self.get_pages_url = "https://fr.wikipedia.org/w/api.php"

    def get_response(self):
        """ Get the json from wikipedia. """
        get_pages_payload = {
            'action': 'query',
            'format': 'json',
            'list': 'geosearch',
            'gscoord': f"{self.latitude}|{self.longitude}"
        }
        r = requests.get(self.get_pages_url, params=get_pages_payload)
        return r.json()

    def get_matching_page(self, response):
        """
            Search for a matching page title with the adress in it.
            If no adress, we pick the first page.
        """
        pages = response['query']['geosearch']
        titles = [page['title'] for page in pages]
        address_list = self.address.split(' ')
        for title in titles:
            title_split = title.split(' ')
            for word in address_list:
                if word in title_split:
                    index = titles.index(title)
                    return titles[index]
        if titles:
            return titles[0]
        else:
            return None

    def get_summary(self, page):
        """ Get the summary from the page chosen"""
        url = f"https://fr.wikipedia.org/api/rest_v1/page/summary/{page}"
        if page:
            r = requests.get(url)
            summary = r.json()['extract']
            return summary

        return None
