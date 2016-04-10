from flask.ext.testing import TestCase
from . import app
from app.data import db

class BaseTestCase(TestCase):
    def create_app(self):
        app.config.from_object('config')
	return app
    def setUp(self):
	app.config['TESTING']=True
	app.config['WTF_CSRF_ENABLED']=False
        db.create_all()
    def tearDown(self):
        #db.session_remove()
        db.drop_all()

