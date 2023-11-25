from flask import Blueprint, jsonify, request
from flask_cors import cross_origin
from controllers.user_controller import userController

user = Blueprint('User', __name__)

@user.route('/user')
def index_user():
    return jsonify({'Bienvenido': 'Entorno de usuarios'})

@user.route('/user/login', methods=['POST'])
@cross_origin()
def insert_user():
    if request.method == 'POST':
        response = userController.getUser(user=request.json)
        return jsonify(response)