#Statement for enabling development environment
DEBUG = True
import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))


BASE_DIR= os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(BASE_DIR, 'app.db')
DATABASE_CONNECT_OPTIONS={}

# Application thrads. common general assumption is
# using 2 per available processor cores - to handle 
# incoming requests using one and performing background
# operations using the other

THREADS_PER_PAGE=2
#Enable protection agains cross-site request forgery (CSRF)
CSRF_ENABLED=True
#Use a secure, unique and absolutely secret key for a signing the data
CSRF_SESSION_KEY = "secret"
#Secret key for signing cookies
SECRET_KEY="secret"

SCHEDULER_VIEWS_ENABLED = True

#Set up email notification
#mail server settings
MAIL_SERVER='localhost'
MAIL_PORT=25
MAIL_USERNAME=None
MAIL_PASSWORD=None
#administrator list
ADMINS=['you@example.com']

#Configuration for uploader files
UPLOAD_FOLDER='data/'
MAX_CONTENT_LENGTH= 50 * 1024 * 1024




