# app/controllers/customer_controller.py

from flask import Blueprint, request, jsonify
from app.models import db
from app.models.customer import Customer
# from app.models.customer import CustomerSchema

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
    

@customer_bp.route('/customer-update/<string:customer_id>', methods=['PUT'])
def update_customer(customer_id):

    print('inside update_customer')
    try:
        # Get the customer from the database
        customer = Customer.query.get(customer_id)
        if not customer:
            return jsonify({"error": "Customer not found"}), 404
        
        # Get the JSON data from the request
        data = request.get_json()
        
        # Update customer fields based on provided data
        customer.company_name = data.get('company_name', customer.company_name)
        customer.contact_name = data.get('contact_name', customer.contact_name)
        customer.contact_title = data.get('contact_title', customer.contact_title)
        customer.address = data.get('address', customer.address)
        customer.city = data.get('city', customer.city)
        customer.region = data.get('region', customer.region)
        customer.postal_code = data.get('postal_code', customer.postal_code)
        customer.country = data.get('country', customer.country)
        customer.phone = data.get('phone', customer.phone)
        customer.fax = data.get('fax', customer.fax)

        # Commit the changes
        db.session.commit()
        
        return jsonify({"message": "Customer updated successfully!"}), 200
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({"error": str(e)}), 500
    

@customer_bp.route('/get-customer/<string:customer_id>', methods=['GET'])
def get_customer(customer_id):
    customer_schema = Customer()
    print('inside get-customer')
    try:
        customer = Customer.query.filter_by(customer_id=customer_id).first()
        print('this is customer',customer)
        print('Company Name:', customer.company_name)
        customer_data = {
            'customer_id': customer.customer_id,
            'company_name': customer.company_name,
            'contact_name': customer.contact_name,
            'contact_title': customer.contact_title,
            'address': customer.address,
            'city': customer.city,
            'region': customer.region,
            'postal_code': customer.postal_code,
            'country': customer.country,
            'phone': customer.phone,
            'fax': customer.fax
        }
        if not customer:
            return jsonify({'error': 'Customer not found'}), 404

        return jsonify(customer_data), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Internal server error