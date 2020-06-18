import os

GOOGLE_API_KEY = ""

try:
    from app.local_settings import *
except ImportError:
    print("local_settings.py n'a pas ete cree.")