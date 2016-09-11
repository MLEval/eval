from e import db
from e.model.model import Model


class Prediction(db.Document):
    mid = db.ObjectIdField(required=True)
    value = db.StringField(max_length=128)

    # User specified identifier of the persisted entity in the client code so
    # that a Result can be matched with a Prediction
    identifier = db.StringField(max_length=128)

    # Note that probability and threshold are both of the positive class.
    threshold = db.DecimalField(min_value=0, max_value=1, precision=2)
    probability = db.DecimalField(min_value=0, max_value=1,
                                  precision=2, required=True)

    @property
    def model(self):
    	Model.objects(id=mid)
