from celery import Celery
from flask_sqlalchemy import SQLAlchemy
from app.mod_photos.models import Photo
from app.data import db

celery = Celery('tasks')
celery.config_from_object('celeryconfig')
#TODO temporal task test
#db.create_all()

def execute_analysis(photo):
	data ={'info':'result!','analysed':True}
	photo.update(**data)

@celery.task
def analyse_document():
    photos = Photo.query.all()
    for photo in photos:
	if not photo.analysed:
		execute_analysis(photo)
