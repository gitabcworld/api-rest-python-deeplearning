from celery.schedules import crontab
from datetime import timedelta

CELERY_BROKER_URL="amqp://guest@localhost//"
CELERYBEAT_SCHEDULE = {
	'every-day': {
		'task': 'tasks.newwinner',
		'schedule': timedelta(days=1),
	}
}
CELERY_TIMEZONE='UTC'
