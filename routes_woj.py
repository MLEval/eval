from app import app # TODO(wojtek) figure out why this needs to be here
from controller import organization as o
from utils import route

########################
# Organization Endpoints
########################


route('/organization/', 'create_organization', o.create_organization, 'POST')
route('/organization/<oid>/', 'get_organization', o.get_organization, 'GET')
route('/organization/<oid>/', 'update_organization', o.update_organization, 'PUT')
route('/organization/all/', 'get_all_organizations', o.get_all_organizations, 'GET')
route('/organization/die/', 'delete_all_organizations', o.delete_all_organizations, 'DELETE')
