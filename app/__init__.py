# app/__init__.py

from flask import Flask
from app.controllers import user_controller

def create_app():
    app = Flask(__name__)
    
    # Register the example blueprint
    app.register_blueprint(user_controller.user_bp)

    return app
