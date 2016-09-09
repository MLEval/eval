import json
from bson import ObjectId

import mongoengine as me

class JSONEncoder(json.JSONEncoder):
    """Class for encoding dicts from pymongo, with ObjectIDs."""
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


def make_serializable(o):
    """Recursively casts mongoengine types to list or dict."""
    if isinstance(o, me.queryset.QuerySet):
        return [make_serializable(e) for e in o]
    elif isinstance(o, me.Document):
        return o.to_mongo()
    return o


def serialize_response(func):
    """Decorator that JSON serializes response."""
    def func_wrapper(*args, **kwargs):
        return JSONEncoder().encode(make_serializable(func(*args, **kwargs)))
    return func_wrapper
