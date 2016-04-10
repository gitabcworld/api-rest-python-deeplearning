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
    #userId = User.select_random_id(User.__tablename__)
    num_users = User.query.count()
    print("Number of users: "+str(num_users))
    if num_users == 0:
	    return -1
    import random
    rand = random.randrange(0,num_users)
    user = User.query.all()[rand]
    Winner.create(**{'name': user.name})
    print("User winner name="+str(user.name))
    
