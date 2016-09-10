from e import db

NAME_MAX_LENGTH = 128


class User(db.Document):
    """User document stores information about a user."""
    email = db.EmailField(required=True, unique=True)

    # What if user belongs to multiple organizations?
    oid = db.ObjectIdField()

    # Extra meta.
    first_name = db.StringField(max_length=NAME_MAX_LENGTH)
    last_name = db.StringField(max_length=NAME_MAX_LENGTH)

    # TODO: add password when we do auth
