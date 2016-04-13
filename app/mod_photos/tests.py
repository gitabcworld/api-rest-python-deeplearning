from flask import url_for
from flask.ext.login import current_user

from app.test_base import BaseTestCase
from app import app

from .models import Photo


class TestModelPhoto(BaseTestCase):
    def test_new_photo(self):
        photo = Photo('carlos')
        self.assertTrue(photo.name,'carlos')

class TestPhotosViews(BaseTestCase):
    def test_post_photo_correct(self):
	
        with self.app.open_resource("test_resources/photo.jpg") as fp:
            with self.client:
                response = self.client.post("/photos/v1.0/photos",data={'file':fp});
		app.logger.debug(response)
		print dir(response)
		self.app.logger.debug(response.json)
		#TODO add assert for correct response
		self.assert_200(response)
    def post_photo_not_allowed_file(self):
	    pass
