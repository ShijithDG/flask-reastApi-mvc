# app/models/__init__.py

from flask_sqlalchemy import SQLAlchemy

# create a SQLalchemy instance
db = SQLAlchemy()

# importing models
from .customer import Customer
from .products import Products
from .orders import Orders
