from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)
db = MongoEngine(app)

@app.route("/")
def hello():
    return "Hello world!"

if __name__ == "__main__":
    app.run()
