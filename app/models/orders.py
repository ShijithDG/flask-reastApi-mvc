from app.models import db


class Orders(db.Model):
    
    __table__name = 'Orders'
    
    order_id = db.Column(db.SmallInteger, primary_key=True, autoincrement=True)
    customer_id = db.Column(db.String(20), db.ForeignKey('customers.customer_id'))  # foreign key 
    employee_id = db.Column(db.SmallInteger)
    order_date = db.Column(db.Date)
    required_date = db.Column(db.Date)
    shipped_date = db.Column(db.Date)
    ship_via = db.Column(db.SmallInteger) 
    freight = db.Column(db.Float)
    ship_name = db.Column(db.String(40))
    ship_address = db.Column(db.String(60))
    ship_city = db.Column(db.String(15))
    ship_region = db.Column(db.String(15))
    ship_postal_code = db.Column(db.String(10))
    ship_country = db.Column(db.String(15))
    
    def __repr__(self) -> str:
        return f'<Products {self.product_name}>'
    