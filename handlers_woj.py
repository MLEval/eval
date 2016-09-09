from flask import request

from app import app
from controller import organization as o


@app.route("/organization/", methods=['POST'])
def organization_create():
    """Create new organization."""
    return o.create_organization()


@app.route("/organization/<oid>/", methods=['GET', 'PUT'])
def organization(oid):
    """Get or update existing porganization."""
    if request.method == 'GET':
        return o.get_organization(oid)
    return o.update_organization(oid)


@app.route("/organization/all/")
def organization_all():
    """Return all organizations."""
    return o.get_all_organizations()


@app.route("/organization/die/", methods=['DELETE'])
def organization_die():
    """Drop organization table."""
    return o.delete_all_organizations()
