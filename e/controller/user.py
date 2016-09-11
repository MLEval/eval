from flask import request

from e.model.organization import Organization
from e.model.user import User
from e.utils import serialize_response


@serialize_response
def create_user():
    """Create new user with email and optionally name."""
    # TODO: handle case where name is not given (maybe make decorator)
    kwargs = {
        'email': request.form['email']
    }
    if 'first_name' in request.form:
        kwargs['first_name'] = request.form['first_name']
    if 'last_name' in request.form:
        kwargs['last_name'] = request.form['last_name']
    if 'oid' in request.form:
        Organization.objects.get_or_404(id=request.form['oid'])
        kwargs['oid'] = request.form['oid']

    return User(**kwargs).save()


@serialize_response
def get_user(uid):
    """Get user with given uid."""
    return User.objects.get_or_404(id=uid)


@serialize_response
def update_user(uid):
    """Get user with given uid."""
    kwargs = request.form.to_dict()
    if 'oid' in kwargs:
        Organization.objects.get_or_404(id=kwargs['oid'])
        kwargs['oid'] = kwargs['oid']

    user = User.objects.get_or_404(id=uid)
    user.modify(**kwargs)
    return user


@serialize_response
def get_all_users():
    """Gets all users."""
    return User.objects.all()


def delete_all_users():
    """Drop user table."""
    User.drop_collection()
    return 'goodbye\n'
