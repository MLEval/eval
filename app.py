from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)
db = MongoEngine(app)

from handlers_woj import *

if __name__ == "__main__":
    app.run(debug=True)
