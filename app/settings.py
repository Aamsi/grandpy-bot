import os

GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')
MAPBOX_TOKEN = os.environ.get('MAPBOX_TOKEN')

PATH_TO_TEST_RESSOURCES = os.path.join('ressources', 'pages_wiki.json')

# Uncomment when testing
# GOOGLE_API_KEY = "12345"

try:
    from app.local_settings import *
except ImportError:
    print("local_settings.py n'a pas ete cree.")
