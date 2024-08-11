
from flask import Blueprint, jsonify, render_template, request

from model import Customer
from app import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
	return render_template('index.html', customers=get_customer_data())

@main.route('/api/customer', methods=["POST"])
def apiCustomerCreate():
	data = request.get_json()
	c = Customer()
	c.city = data['city']
	c.name = data['name']
	c.telephone = data['telephone']
	c.telephoneCountryCode = data['telephoneCountryCode']
	db.session.add(c)
	db.session.commit()
	return jsonify({
		"id": c.id,
		"name": c.name,
		"city": c.city,
		"telephone": c.telephone ,
		"telephoneCountryCode": c.telephoneCountryCode,
	}), 201

@main.route('/api/customer/<id>')	
def apiCustomerRead(id):
	c = Customer.query.filter_by(id=id).first_or_404()
	return jsonify({
		"id": c.id,
		"name": c.name,
		"city": c.city,
		"telephone": c.telephone ,
		"telephoneCountryCode": c.telephoneCountryCode,
	}), 200

@main.route('/api/customer/<id>', methods=["PUT"])
def apiCustomerUpdate(id):
	data = request.get_json()
	c = Customer.query.filter_by(id=id).first_or_404()
	c.city = data['city']
	c.name = data['name']
	c.telephone = data['telephone']
	c.telephoneCountryCode = data['telephoneCountryCode']
	db.session.commit()
	return jsonify({
		"id": c.id,
		"name": c.name,
		"city": c.city,
		"telephone": c.telephone ,
		"telephoneCountryCode": c.telephoneCountryCode,
	}), 200

@main.route('/api/customer')
def apiCustomerList():
	return jsonify(get_customer_data())

def get_customer_data():
	return [
		{
			"id": c.id,
			"name": c.name,
			"city": c.city,
		}
		for c in Customer.query.all()
	]