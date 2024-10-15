# app/controllers/user_controller.py

from flask import Blueprint, jsonify

user_bp = Blueprint('user', __name__)

# Define a route for getting a list of users
@user_bp.route('/', methods=['GET'])
def get_users():
    return jsonify({"users": ["Alice", "Bob", "Charlie"]})
