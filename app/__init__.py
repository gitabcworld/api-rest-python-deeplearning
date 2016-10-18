from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
#from celery import Celery
#from celery.decorators import periodic_task
from datetime import timedelta
from celery.task.schedules import crontab
from app.data import db
from flask_login import LoginManager

app = Flask(__name__)
app.logger.debug("")

app.config.from_object('config')

'''
import logging
handler = logging.FileHandler('/home/aberenguel/www/api-rest-python-deeplearning/app.log')  # errors logged to this file
handler.setLevel(logging.ERROR) # only log errors and above
app.logger.addHandler(handler)  # attach the handler to the app's logger                                                                                                                                                                                                                                        
app.logger.debug('AAAAAAAA')
'''

#Bootstrap extension
Bootstrap(app)

#Login manager
login_manager = LoginManager()
login_manager.init_app(app)

#Build the database:
#This will create the database file using SQLAlchemy
db.init_app(app)
db.app = app
db.create_all()

#Load modules
from app.mod_photos.controllers import mod_photos as photos_module
from app.mod_main.controllers import mod_main as main_module

app.register_blueprint(photos_module)
app.register_blueprint(main_module)

#email logger
if not app.debug:
	from config import basedir, ADMINS,MAIL_SERVER, MAIL_PORT, MAIL_USERNAME, MAIL_PASSWORD
	import logging
	from logging.handlers import SMPTHandler
	credentials = None
	if MAIL_USERNAME or MAIL_PASSWORD:
		credentials = (MAIL_USERNAME, MAIL_PASSWORD)
	mail_handler = SMTPHandler((MAIL_SERVER,MAIL_PORT),'no-reply@'+MAIL_SERVER,ADMINS, 'app failure',credentials)
	mail_handler.setLevel(logging.ERROR)
	app.logger.addHandler(mail_handler)


#if not app.debug:
import logging
from logging.handlers import RotatingFileHandler
file_handler = RotatingFileHandler('app.log','a',1*1024*1024,10)
file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
app.logger.setLevel(logging.INFO)
file_handler.setLevel(logging.INFO)
app.logger.addHandler(file_handler)
app.logger.info('app startup')
