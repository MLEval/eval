from flask import Flask
from mongokat import Collection, Document

class SampleDocument(Document):

        def my_sum(self):
                return self["a"] + self["b"]

class SampleCollection(Collection):
        document_class = SampleDocument

        def find_by_a(self, a_value):
                return self.find_one({"a": a_value})

# Then use it in your code like this:

from pymongo import MongoClient
client = MongoClient()
Sample = SampleCollection(collection=client.my_db.my_col)

app = Flask(__name__)

@app.route("/")
def hello():
    Sample.insert({"a": 1, "b": 2})
    five = Sample.find_by_a(1)
    return str(five.my_sum())

if __name__ == "__main__":
    app.run()
