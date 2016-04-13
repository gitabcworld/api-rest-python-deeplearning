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
    def test_post_photo(self):
	
	app.logger.debug("Executing test photo")
        with self.app.open_resource("test_resources/photo.jpg") as fp:
            with self.client:
                response = self.client.post("/photos/v1.0/photos",data={'file':fp});
		app.logger.debug(response)
