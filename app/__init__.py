# app/__init__.py

from flask import Flask
# from app.controllers import user_controller
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    app.config.from_object(Config)
    
    db.init_app(app)
    
    # Register the example blueprint
    # app.register_blueprint(user_controller.user_bp)
    from app.controllers import user_controller  # Add any other controllers here
    app.register_blueprint(user_controller.user_bp)


    return app
