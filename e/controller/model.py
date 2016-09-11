from flask import request

from e.model.organization import Organization
from e.model.user import User
from e.model.model import Model
from e.utils import serialize_response


@serialize_response
def create_model():
    Organization.objects.get_or_404(id=request.form['oid'])

    # Actually when we add auth, make the creator the current guy
    # so no need for this
    User.objects.get_or_404(id=request.form['creator'])

    # TODO(rossem): make sure classes dont have the same name

    return Model(**{
        'name': request.form['name'],
        'oid': request.form['oid'],
        'creator': request.form['creator'],
        'positive_class': request.form.get('positive_class'),
        'negative_class': request.form.get('negative_class')
    }).save()

@serialize_response
def get_model(id):
    return Model.objects.get_or_404(id=id)

@serialize_response
def update_model(id):
    model = Model.objects.get_or_404(id=id)
    model.modify(**{
        'name': request.form.get('name'),
        'positive_class': request.form.get('positive_class'),
        'negative_class': request.form.get('negative_class')
    })
    return model

@serialize_response
def get_user_models(uid):
    return Model.objects(creator=uid)

@serialize_response
def get_org_models(oid):
    return Model.objects(oid=oid)
