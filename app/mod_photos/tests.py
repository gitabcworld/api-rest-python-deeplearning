from flask import url_for
from flask.ext.login import current_user

from app.test_base import BaseTestCase
from app import app
from .models import Photo


class TestModelPhoto(BaseTestCase):
	def test_new_photo(self):
		photo = Photo()

'''
from .models import User
from app.mod_auth.forms import LoginForm, RegisterForm
'''

'''
class TestAuthLoginForms(BaseTestCase):
    def test_validate_login_form(self):
        form = LoginForm(email='mcflurry0@gmail.com',password='example')
        self.assertTrue(form.validate())
    
    def test_validate_login_invalid_email_form(self):
        form = LoginForm(email='mcflurry0',password='example')
	self.assertFalse(form.validate())
    
    def test_validate_login_without_password_form(self):
        form = LoginForm(email='mcflurry0@gmail.com',password='')
        self.assertFalse(form.validate())
        
class TestAuthRegisterForms(BaseTestCase):
    def test_validate_register_form(self):
        form = RegisterForm(email='mcflurry0@gmail.com',password='example',name='Carlos Baez')
        self.assertTrue(form.validate())
    def test_validate_register_invalid_email_form(self):
        form = RegisterForm(email='mcflurry0',password='example',name='Carlos Baez')
        self.assertFalse(form.validate())   
    def test_validate_register_invalid_password_form(self):
        form = RegisterForm(email='mcflurry0@gmail.com',password='',name='Carlos Baez')
        self.assertFalse(form.validate())
    def test_validate_register_invalid_name_form(self):
        form = RegisterForm(email='mcflurry0@gmail.com',password='example',name='')
        self.assertFalse(form.validate())

class TestAuthViews(BaseTestCase):
    def test_signin(self):
	with self.client: 
            response = self.client.post(url_for('auth.signin')
			    ,data={"email":"joe@joes.com","password":"pass"})

            self.assert_200(response)

    def test_register(self):
	with self.client:
            response = self.client.post(url_for('auth.register')
			    ,data={"email":"joe@joes.com","password":"pass","name":"Carlos Baez Ruiz"})

            response = self.client.post(url_for('auth.signin')
			    ,data={"email":"joe@joes.com","password":"pass","name":"Carlos Baez Ruiz"})

	    response = self.client.get(url_for('users.home'))
	    self.assert_200(response)
            self.assertIn("hello,",response.data)
'''
