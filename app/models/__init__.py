# app/models/__init__.py

from flask_sqlalchemy import SQLAlchemy

# Create a SQLAlchemy instance
db = SQLAlchemy()

# Import your models

# ---------------------------------------------
from .customer import Customer
# from .product import Product
# from .order import Order
