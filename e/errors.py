from flask import jsonify

from e import app


# Common error messages
ORG_NOT_FOUND = 'Organization not found.'
USER_NOT_FOUND = 'User not found.'
MODEL_NOT_FOUND = 'Model not found.'


class APIError(Exception):
    status_code = 400

    def __init__(self, message, status_code=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self):
        return {'error': self.message}


@app.errorhandler(APIError)
def handle_api_error(e):
    response = jsonify(e.to_dict())
    response.status_code = e.status_code
    return response
