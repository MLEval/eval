import json
from bson import ObjectId
from functools import wraps

from app import app
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
    @wraps(func)
    def func_wrapper(*args, **kwargs):
        return JSONEncoder().encode(make_serializable(func(*args, **kwargs)))
    return func_wrapper


def route(rule, endpoint, view_func, method):
    """Adds route to app."""
    assert rule[-1] == '/', 'rule should end in a trailing slash'
    app.add_url_rule(rule, endpoint, view_func, methods=[method])
