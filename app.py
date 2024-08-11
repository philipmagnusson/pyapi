import os
from flask import Flask
from flask_migrate import Migrate
from config import DevConfig, ProdConfig
from model import db, seedData, Customer

def create_app():
	app = Flask(__name__)
	
	if os.getenv("RUNENVIRONMENT") == 'production':
		print('!!Kör i PRODUCTION MODE!!')
		app.config.from_object(ProdConfig)
	else:
		app.config.from_object(DevConfig)

	db.init_app(app)
	migrate = Migrate(app, db)

	from routes import main
	app.register_blueprint(main)

	with app.app_context():
		db.create_all()
		seedData(db)	
	return app

if __name__ == '__main__':
	app = create_app()
	app.run(debug=True)