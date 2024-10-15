# app/controllers/customer_controller.py

from flask import Blueprint, request, jsonify
from app.models import db
from app.models.customer import Customer

customer_bp = Blueprint('customer', __name__)

@customer_bp.route('/add-customer', methods=['POST'])
def add_customer():
    print("Received POST request") 
    data = request.get_json()  # Expecting JSON data
    print('this is incomming data', data)
    try:
        new_customer = Customer(
            customer_id=data['customer_id'],
            company_name=data['company_name'],
            contact_name=data.get('contact_name'),
            contact_title=data.get('contact_title'),
            address=data.get('address'),
            city=data.get('city'),
            region=data.get('region'),
            postal_code=data.get('postal_code'),
            country=data.get('country'),
            phone=data.get('phone'),
            fax=data.get('fax')
        )
        
        db.session.add(new_customer)
        db.session.commit()
        
        return jsonify({'message': 'Customer added successfully!', 'customer_id': new_customer.customer_id}), 201
    
    except Exception as e:
        db.session.rollback()  # Rollback in case of an error
        return jsonify({'error': str(e)}), 400
