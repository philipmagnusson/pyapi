import random
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Customer(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50), unique=False, nullable=False)
	city = db.Column(db.String(40), unique=False, nullable=False)
	telephoneCountryCode = db.Column(db.Integer, unique=False, nullable=False)
	telephone = db.Column(db.String(20), unique=False, nullable=False)

def seedData(db):
	cities = ["Stockholm", "Västerås", "Södertälje"]
	countryCodes = [46,47,44]
	count = Customer.query.count()
	for i in range(count):
		customer = Customer()
		customer.name = "Customer" + str(i)
		customer.telephoneCountryCode = random.choice(countryCodes)
		customer.telephone = random.randint(10000000,999999999)
		customer.city = random.choice(cities)
		db.session.add(customer)
		db.session.commit()	
