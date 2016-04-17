from flask.ext.testing import TestCase
from . import app
from app.data import db

class BaseTestCase(TestCase):
    #FIXME DEAD CODE??
    def create_app(self):
        app.config.from_object('config')
	return app
    def setUp(self):
	app.config['WTF_CSRF_ENABLED']=False
	app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///:memory:'
	app.config['TESTING']=True
	#set up memory database
	db.app = app
	db.create_all()
    def tearDown(self):
        #db.session_remove()
        db.drop_all()

