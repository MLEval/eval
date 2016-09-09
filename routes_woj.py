from app import app
from controller import organization as o

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
