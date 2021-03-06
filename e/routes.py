import json
import time

from flask import request, Response

from e import app
from e.controller import (
    organization as o,
    user as u,
    model as m,
    prediction as p,
    result as r
)

app.add_url_rule('/', 'root', lambda: app.send_static_file('index.html'))


@app.route('/api/comments', methods=['GET', 'POST'])
def comments_handler():
    with open('comments.json', 'r') as f:
        comments = json.loads(f.read())

    if request.method == 'POST':
        new_comment = request.form.to_dict()
        new_comment['id'] = int(time.time() * 1000)
        comments.append(new_comment)

        with open('comments.json', 'w') as f:
            f.write(json.dumps(comments, indent=4, separators=(',', ': ')))

    return Response(
        json.dumps(comments),
        mimetype='application/json',
        headers={
            'Cache-Control': 'no-cache',
            'Access-Control-Allow-Origin': '*'
        }
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

########################
# Model Endpoints
########################

app.add_url_rule('/model/', 'create_model',
                 m.create_model, methods=['POST'])

app.add_url_rule('/model/<id>/', 'get_model',
                 m.get_model, methods=['GET'])

app.add_url_rule('/model/<id>', 'update_model',
                 m.update_model, methods=['PUT'])

app.add_url_rule('/user/<uid>/models/', 'get_user_models',
                 m.get_user_models, methods=['GET'])

app.add_url_rule('/organization/<oid>/models/', 'get_org_models',
                 m.get_org_models, methods=['GET'])

########################
# Prediction Endpoints
########################

app.add_url_rule('/model/<mid>/predictions', 'add_model_prediction',
                 p.add_model_prediction, methods=['POST'])

app.add_url_rule('/model/<mid>/predictions', 'get_model_predictions',
                 p.get_model_predictions, methods=['GET'])

########################
# Result Endpoints
########################

app.add_url_rule('/model/<mid>/results', 'add_model_result',
                 r.add_model_result, methods=['POST'])

app.add_url_rule('/model/<mid>/results', 'get_model_results',
                 r.get_model_results, methods=['GET'])
