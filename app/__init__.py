from flask import Flask

app_bot = Flask(__name__)

from app import routes  # noqa: E402, F401
