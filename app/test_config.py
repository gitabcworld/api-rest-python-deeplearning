import unittest
import os
from app import app
from flask.ext.testing import TestCase

class TestConfig(TestCase):
	def create_app(self):
		app.config.from_object('config')
		return app

	def test_app_is_config(self):
		self.assertTrue(app.config['THREADS_PER_PAGE'] == 2)
		self.assertTrue(app.config['CSRF_ENABLED'] == True)
		self.assertTrue(app.config['SCHEDULER_VIEWS_ENABLED'] == True)


