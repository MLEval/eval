from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__, static_url_path='', static_folder='public')
db = MongoEngine(app)
