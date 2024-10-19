# app/__init__.py

from flask import Flask
# from app.controllers import user_controller
from flask_sqlalchemy import SQLAlchemy
from config import Config
from app.models import db 




def create_app():
    app = Flask(__name__)
    
    app.config.from_object(Config)
    
    db.init_app(app)
    
    with app.app_context():
        db.create_all()  # This creates the tables based on your models
    
    # Register the example blueprint
    # app.register_blueprint(user_controller.user_bp)
    from app.controllers import user_controller  # Add any other controllers here
    from app.controllers import customers_controller
    from app.controllers import products_controller
    from app.controllers import orders_controller
    app.register_blueprint(customers_controller.customer_bp)
    app.register_blueprint(user_controller.user_bp)
    app.register_blueprint(products_controller.products_bp)
    app.register_blueprint(orders_controller.orders_bp)


    return app
