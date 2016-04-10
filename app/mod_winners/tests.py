from flask import url_for
from flask.ext.login import current_user

from app.test_base import BaseTestCase
from app import app

class TestWinnerViews(BaseTestCase):
    def test_not_permitted_winner(self):
	with self.client: 
            response = self.client.post(url_for('users.home'))
	    self.assert_401(response)
