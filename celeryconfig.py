from celery.schedules import crontab
from datetime import timedelta

CELERY_BROKER_URL="amqp://guest@localhost//"
CELERYBEAT_SCHEDULE = {
	'every-day': {
		'task': 'tasks.analyse_document',
		'schedule': timedelta(seconds=5),
	}
}
CELERY_TIMEZONE='UTC'
