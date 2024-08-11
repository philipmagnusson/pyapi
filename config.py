import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	DEBUG = False

class ProdConfig(Config):
	SQLALCHEMY_DATABASE_URI = 'postgresql://root:passwd@postgresserver/customerdb' #fix me

class DevConfig(Config):
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.sqlite')
	DEBUG = True