from app import db

class Organization(db.Document):
    name = db.StringField(required=True)
