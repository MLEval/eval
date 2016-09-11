from e import db


class Model(db.Document):
    name = db.StringField(max_length=128, required=True)
    oid = db.ObjectIdField(required=True)
    creator = db.ObjectIdField(required=True)
    positive_class = db.StringField(max_length=128, default='Positive')
    negative_class = db.StringField(max_length=128, default='Negative')

    @property
    def classes(self):
        return [self.positive_class, self.negative_class]
