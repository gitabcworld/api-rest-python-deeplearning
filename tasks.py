from celery import Celery
from flask.ext.sqlalchemy import SQLAlchemy
from app.mod_photos.models import Photo
from app.data import db

celery = Celery('tasks')
celery.config_from_object('celeryconfig')
#TODO temporal task test
db.create_all()

@celery.task
def newwinner():
    pass
    
