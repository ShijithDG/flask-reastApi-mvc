from flask import Blueprint, jsonify, request
from app.models import db
from app.models import Orders


orders_bp = Blueprint('orders', __name__)

@orders_bp.route('/add-orders', methods=['POST'])
def add_orders():

    print('inside add order api')
    try:
        
        data = request.get_json()
        new_order = Orders(
            order_id=data['order_id'],
            customer_id=data.get('customer_id'),
            employee_id=data.get('employee_id'),
            order_date=data.get('order_date'),  # Ensure this is a date object
            required_date=data.get('required_date'),  # Ensure this is a date object
            shipped_date=data.get('shipped_date'),  # Ensure this is a date object or None
            ship_via=data.get('ship_via'),
            freight=data.get('freight'),
            ship_name=data.get('ship_name'),
            ship_address=data.get('ship_address'),
            ship_city=data.get('ship_city'),
            ship_region=data.get('ship_region'),
            ship_postal_code=data.get('ship_postal_code'),
            ship_country=data.get('ship_country')
        )
        
        db.session.add(new_order)
        db.session.commit()
        
        return jsonify({'message': 'Customer added successfully!', 'customer_id': new_order.order_id}), 201

        
    except Exception as e:
        db.session.rollback()
        print(f'error : {e}')
        return jsonify({"message":"server error "}), 500
    
@orders_bp.route('/update-orders/<string:order_id>', methods=['PUT'])
def update_order(order_id):
    try:
        orders = Orders.query.get(order_id)
        
        if not orders:
            return jsonify({"message":"order not found"})
        
        data = request.get_json()
        
        orders.order_id = data.get('order_id', orders.order_id),
        orders.customer_id = data.get('customer_id', orders.customer_id),
        orders.employee_id = data.get('employee_id', orders.employee_id),
        orders.order_date = data.get('order_date', orders.order_date),
        orders.required_date = data.get('required_date', orders.required_date),
        orders.shipped_date = data.get('shipped_date', orders.shipped_date),
        orders.ship_via = data.get('ship_via', orders.ship_via),
        orders.freight = data.get('freight', orders.freight)
        orders.ship_name = data.get('ship_name', orders.ship_name),
        orders.ship_address = data.get('ship_address', orders.ship_address),
        orders.ship_city = data.get('ship_city', orders.ship_city),
        orders.ship_region = data.get('ship_region', orders.ship_region),
        orders.ship_postal_code = data.get('ship_postal_code', orders.ship_postal_code),
        orders.ship_country = data.get('ship_country', orders.ship_country),
        
        db.session.commit()
        return jsonify({'message': 'order updated successfully'})
    
    except Exception as e:
        
        db.session.rollback()
        print(f"error : {e}")
        return jsonify({'message': 'server error'}), 500