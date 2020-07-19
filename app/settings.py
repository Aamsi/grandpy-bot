import os

# Get the environment variables from Heroku app
GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')
MAPBOX_TOKEN = os.environ.get('MAPBOX_TOKEN')

# Used in test_wiki.py
PATH_TO_TEST_RESSOURCES = os.path.join('ressources', 'pages_wiki.json')

# If we want to test locally, we use variables in local_settings.py
try:
    from app.local_settings import *  # noqa: F401, F403
except ImportError:
    print("local_settings.py n'a pas ete cree.")
