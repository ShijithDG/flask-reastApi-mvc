

from app.models import db

class Products(db.Model):
    __tablename__ = 'products'
    
    product_id = db.Column(db.SmallInteger, primary_key=True)
    product_name = db.Column(db.String(40), nullable=False)
    supplier_id = db.Column(db.SmallInteger)  # Adjust according to the actual foreign key
    category_id = db.Column(db.SmallInteger)  # Adjust according to the actual foreign key
    quantity_per_unit = db.Column(db.String(20))
    unit_price = db.Column(db.Numeric(10, 2))  # Using Numeric for better precision
    units_in_stock = db.Column(db.SmallInteger)
    units_on_order = db.Column(db.SmallInteger)
    reorder_level = db.Column(db.SmallInteger)
    discontinued = db.Column(db.Boolean, nullable=False)  # Changed to Boolean for clarity
    
    def __repr__(self) -> str:
        return f'<Products {self.product_name}>'
    
    
    