# app/models/customer.py

from app.models import db

class Customer(db.Model):
    __tablename__ = 'customers'
    
    customer_id = db.Column(db.String(20), primary_key=True)  # Set a length for VARCHAR
    company_name = db.Column(db.String(40), nullable=False)
    contact_name = db.Column(db.String(30))
    contact_title = db.Column(db.String(30))
    address = db.Column(db.String(60))
    city = db.Column(db.String(15))
    region = db.Column(db.String(15))
    postal_code = db.Column(db.String(10))
    country = db.Column(db.String(15))
    phone = db.Column(db.String(24))
    fax = db.Column(db.String(24))

    def __repr__(self):
        return f'<Customer {self.company_name}>'
    

    