from flask import request

from e.model.organization import Organization
from e.utils import serialize_response


@serialize_response
def create_organization():
    """Create new organization and return object."""
    # TODO: handle case where name is not given (maybe make decorator)
    return Organization(name=request.form['name']).save()


@serialize_response
def get_organization(oid):
    """Get organization with given oid."""
    return Organization.objects.get_or_404(id=oid)


@serialize_response
def update_organization(oid):
    """Update organization and return."""
    kwargs = request.form.to_dict()
    org = Organization.objects.get_or_404(id=oid)
    org.modify(**kwargs)
    return org


@serialize_response
def get_all_organizations():
    """Gets all organizations."""
    return Organization.objects.all()


def delete_all_organizations():
    """Drop organization table."""
    Organization.drop_collection()
    return 'goodbye\n'
