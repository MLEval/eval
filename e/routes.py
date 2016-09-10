from e import app
from e.controller import (
    organization as o,
    user as u
)

########################
# Organization Endpoints
########################

app.add_url_rule('/organization/', 'create_organization',
                 o.create_organization, methods=['POST'])
app.add_url_rule('/organization/<oid>/', 'get_organization',
                 o.get_organization, methods=['GET'])
app.add_url_rule('/organization/<oid>/', 'update_organization',
                 o.update_organization, methods=['PUT'])
app.add_url_rule('/organization/all/', 'get_all_organizations',
                 o.get_all_organizations, methods=['GET'])
app.add_url_rule('/organization/die/', 'delete_all_organizations',
                 o.delete_all_organizations, methods=['DELETE'])

########################
# User Endpoints
########################

app.add_url_rule('/user/', 'create_user',
                 u.create_user, methods=['POST'])
app.add_url_rule('/user/<uid>/', 'get_user',
                 u.get_user, methods=['GET'])
app.add_url_rule('/user/<uid>/', 'update_user',
                 u.update_user, methods=['PUT'])
app.add_url_rule('/user/all/', 'get_all_users',
                 u.get_all_users, methods=['GET'])
app.add_url_rule('/user/die/', 'delete_all_users',
                 u.delete_all_users, methods=['DELETE'])
