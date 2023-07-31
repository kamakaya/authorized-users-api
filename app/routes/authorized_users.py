from flask import Blueprint, request, jsonify
from ..models.authorized_users import db, AuthorizedUsers

authorized_users_blueprint = Blueprint('authorized_users', __name__)

# @authorized_users_blueprint.route('/authorized_users', methods=['GET'])
# def hello():
#     return "Hello World!"

@authorized_users_blueprint.route('/authorized_users', methods=['POST'])
def add_authorized_user():
    data = request.get_json()
    new_authorized_user = AuthorizedUsers(
        user_name=data['user_name'],
        user_email=data['user_email'],
        manager_name=data['manager_name'], 
        project_name=data['project_name']
    )
    db.session.add(new_authorized_user)
    db.session.commit()
    return jsonify({"message": "Authorized User created"}), 201

@authorized_users_blueprint.route('/authorized_users', methods=['GET'])
def get_authorized_users():
    authorized_users = AuthorizedUsers.query.all()
    output = []
    for authorized_user in authorized_users:
        authorized_user_data = {}
        authorized_user_data['id'] = authorized_user.id
        authorized_user_data['user_name'] = authorized_user.user_name
        authorized_user_data['user_email'] = authorized_user.user_email
        authorized_user_data['manager_name'] = authorized_user.manager_name
        authorized_user_data['project_name'] = authorized_user.project_name
        output.append(authorized_user_data)
    return jsonify({"authorized_users": output})

@authorized_users_blueprint.route('/authorized_users/<id>', methods=['GET'])
def get_one_authorized_user(id):
    authorized_user = AuthorizedUsers.query.get(id)
    if not authorized_user:
        return jsonify({"message": "No authorized_user found!"})
    authorized_user_data = {}
    authorized_user_data['id'] = authorized_user.id
    authorized_user_data['user_name'] = authorized_user.user_name
    authorized_user_data['user_email'] = authorized_user.user_email
    authorized_user_data['manager_name'] = authorized_user.manager_name
    authorized_user_data['project_name'] = authorized_user.project_name
    return jsonify({"authorized_user": authorized_user_data})

@authorized_users_blueprint.route('/authorized_users/<id>', methods=['PUT'])
def update_authorized_user(id):
    data = request.get_json()
    authorized_user = AuthorizedUsers.query.get(id)
    if not authorized_user:
        return jsonify({"message": "No authorized_user found!"})
    authorized_user.user_name = data['user_name']
    authorized_user.user_email = data['user_email']
    authorized_user.manager_name = data['manager_name']
    authorized_user.project_name = data['project_name']
    db.session.commit()
    return jsonify({"message": "authorized_user updated!"})

@authorized_users_blueprint.route('/authorized_users/<id>', methods=['DELETE'])
def delete_authorized_user(id):
    authorized_user = AuthorizedUsers.query.get(id)
    if not authorized_user:
        return jsonify({"message": "No authorized_user found!"})
    db.session.delete(authorized_user)
    db.session.commit()
    return jsonify({"message": "authorized_user deleted!"})