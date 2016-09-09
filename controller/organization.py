from flask import request

from model.organization import Organization
from utils import serialize_response


@serialize_response
def create_organization():
    """Create new organization and return object."""
    return Organization(name=request.form['name']).save()


@serialize_response
def get_organization(oid):
    """Get organization with given oid."""
    return Organization.objects.get_or_404(id=oid)


@serialize_response
def update_organization(oid):
    """Update organization and return."""
    kwargs = {'name': request.form['name']}
    org = Organization.objects.get_or_404(id=oid)
    if org.modify(**kwargs):
        return org
    return None


@serialize_response
def get_all_organizations():
    """Gets all organizations."""
    return Organization.objects


def delete_all_organizations():
    """Drop organization table."""
    Organization.drop_collection()
    return 'goodbye\n'
