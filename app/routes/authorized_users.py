from flask import Blueprint, request, jsonify
# from ..models.project import db, Project

authorized_users_blueprint = Blueprint('authorized_users', __name__)

@authorized_users_blueprint.route('/', methods=['GET'])
def hello():
    return "Hello World!"

# @app.route('/')
# def hello():
#     return "Hello World!"