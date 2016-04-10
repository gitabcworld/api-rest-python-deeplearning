#import Form and RecaptchaField

from flask.ext.wtf import Form 
from wtforms import TextField, PasswordField, StringField
from wtforms.validators import Required, Email, EqualTo, DataRequired


class LoginForm(Form):
    email = StringField('email',[Email(),DataRequired(message='Forgot your enail address?')])
    password = PasswordField('password',[DataRequired(message='Must provide a password')])

class RegisterForm(Form):
    email = StringField('email',[Email(),DataRequired(message='Forgot your enail address?')])
    password = PasswordField('password',[DataRequired(message='Must provide a password')])
    name = StringField('Display Name',[DataRequired(message='Must provide a name')])
