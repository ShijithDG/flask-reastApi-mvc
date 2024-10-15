# app/controllers/user_controller.py

from flask import Blueprint, jsonify
from app import db
from sqlalchemy import text

user_bp = Blueprint('user', __name__)

# Define a route for getting a list of users
@user_bp.route('/', methods=['GET'])
def get_users():
    try:
        # Perform a simple query to test the connection
        db.session.execute(text('SELECT 1'))
        return jsonify({"message": "Database connection successful!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
