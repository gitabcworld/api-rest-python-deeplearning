from celery import Celery
from flask.ext.sqlalchemy import SQLAlchemy
from app.mod_winners.models import Winner
from app.mod_auth.models import User
from app.data import db

celery = Celery('tasks')
celery.config_from_object('celeryconfig')
#TODO temporal task test
db.create_all()

@celery.task
def newwinner():
    pass
    
