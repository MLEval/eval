from e import db
from e.model.model import Model
from e.model.prediction import Prediction


class Result(db.Document):
    mid = db.ObjectIdField(required=True)
    pid = db.ObjectIdField(required=True)
    identifier = db.StringField(max_length=128)
    value = db.StringField(max_length=128)

    @property
    def model(self):
        return Model.objects.get(id=self.mid)

    @property
    def prediction(self):
        return Prediction.objects.get(id=self.pid)
