

from flask import Blueprint, jsonify , request
from app.models import db
from app.models import Products

products_bp = Blueprint('products', __name__)

@products_bp.route('/add-product', methods = ['POST'])
def add_products():
    print('inside add products')
    data = request.get_json()
    print(data,'this is data from user')
    try:
        
        new_product = Products(
            product_id=data['product_id'],
            product_name=data['product_name'],
            supplier_id=data.get('supplier_id'),
            category_id=data.get('category_id'),
            quantity_per_unit=data.get('quantity_per_unit'),
            unit_price=data.get('unit_price'),
            units_in_stock=data.get('units_in_stock'),
            units_on_order=data.get('units_on_order'),
            reorder_level=data.get('reorder_level'),
            discontinued=data.get('discontinued'),
        )
        db.session.add(new_product)  
        db.session.commit()
        
        return jsonify({'message': 'Customer added successfully!', 'customer_id': new_product.product_id}), 201
    
    except Exception as e:
        
        db.session.rollback()
        
        print(f"error : {e}")
        return jsonify({'error': "server error"})
    

@products_bp.route('/product-update/<string:product_id>', methods=['PUT'])
def update_product(product_id):
    print('inside the update product')
    
    try :
        
        product = Products.query.get(product_id)
        
        if not product :
            return jsonify({'message' : 'no data found'}), 404
        
        data = request.get_json()
        
        # product.product_id = data.get('product_id', product.product_id),
        product.product_name = data.get('product_name', product.product_name),
        product.supplier_id = data.get('supplier_id', product.supplier_id),
        product.category_id = data.get('category_id', product.category_id),
        product.quantity_per_unit = data.get('quantity_per_unit', product.quantity_per_unit),
        product.unit_price = data.get('unit_price', product.unit_price),
        product.units_in_stock = data.get('units_in_stock', product.units_in_stock),
        product.units_on_order = data.get('units_on_order', product.units_on_order),
        product.reorder_level = data.get('reorder_level', product.reorder_level),
        product.discontinued = data.get('discontinued', product.discontinued)

        db.session.commit()
        return jsonify({"message": "Customer updated successfully!"}), 200

    except Exception as e:
        
        db.session.rollback()
        print(f'error : {e}')
        return jsonify({"error" :"server error "}), 500
    
@products_bp.route('/get-product-detail/<string:product_id>', methods=['GET'])
def get_product_detail(product_id):
    
    print('inisder get product', product_id)
    try:
        product = Products.query.filter_by(product_id = product_id).first()
        if not product:
            return jsonify({"message" : "item is not found"})
        product_detail = {
            "product_id" : product.product_id,
            "product_name" : product.product_name,
            "supplier_id" : product.supplier_id,
            "category_id" : product.category_id,
            "quantity_per_unit" : product.quantity_per_unit,
            "unit_price" : product.unit_price,
            "units_in_stock" : product.units_in_stock,
            "units_on_order" : product.units_on_order,
            "reorder_level" : product.reorder_level,
            "discontinued" : product.discontinued
        }
        return jsonify(product_detail)
    except Exception as e :
        print(f"server error {e}")
        return jsonify({'message': 'server error'}), 500
        
