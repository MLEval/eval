from e import db


class Organization(db.Document):
    """Organization document stores information about a company."""
    name = db.StringField(required=True)

    # TODO: add relationship to models
    # TODO: add relationship to users
