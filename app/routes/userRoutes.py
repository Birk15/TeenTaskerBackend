from flask import Blueprint
from app.controllers.userController import users_get, user_add

users_bp = Blueprint('users', __name__)

@users_bp.route("/get_users", methods=['GET'])
def get_users():
    return users_get()

@users_bp.route("/add_user", methods=['POST'])
def add_user():
    return user_add()

def setup_user_routes(app):
    # Blueprint in der App registrieren
    app.register_blueprint(users_bp)