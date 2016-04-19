from flask import url_for, jsonify, json
from flask.ext.login import current_user

from app.test_base import BaseTestCase
from app import app

from .models import Photo
from factory_responses import FactoryResponse
from app.data import db

def create_photo(number_users):
    return [Photo.create(**{'uuid': str(index+1), 'filepath': 'test'+str(index+1)+'.jpg'}) for index in range(0,number_users) ]

class TestModelPhoto(BaseTestCase):
    def test_new_photo(self):
        photo = Photo('1','/test/photo.png')
        self.assertTrue(photo.uuid,'1')
        self.assertTrue(photo.filepath,'/test/photo.png')
class TestFactoryResponses(BaseTestCase):
	responses = None
	@classmethod
	def setUpClass(cls):
		cls.responses = FactoryResponse()
	@classmethod
	def tearDownClass(cls):
		cls.responses = None

	def test_200_correct(self):
		#TODO add respnse
		resp=self.responses.new200()
		self.assertTrue(resp.status_code==200)
		self.assertTrue(resp.content_type=="application/json")
	def test_201_correct(self):
		empty_data = {}
		resp=self.responses.new201(empty_data)
		self.assertTrue(resp.status_code==201)
		self.assertTrue(resp.content_type=="application/json")
	def test_202_correct(self):
		resp=self.responses.new202()
		self.assertTrue(resp.status_code==202)
		self.assertTrue(resp.content_type=="application/json")

class TestPhotosViews(BaseTestCase):
    def test_post_photo_correct(self):
        with self.app.open_resource("test_resources/photo.jpg") as fp:
            with self.client:
                response = self.client.post("/photos/v1.0/photos",data={'file':fp});
		app.logger.debug(response)
		print dir(response)
		self.app.logger.debug(response.json)
		#TODO add assert for correct response
		self.assertTrue(response.status_code == 201)

    def test_post_photo_not_allowed_file(self):
        with self.app.open_resource("test_resources/photo.txt") as fp:
             with self.client:
                response = self.client.post("/photos/v1.0/photos",data={'file':fp});
		app.logger.debug(response)
		#self.app.logger.debug(response.json)
		#TODO add assert for correct response
		self.assertTrue(response.status_code == 202)

    def test_get_photo_correct(self):
	#fake information
	data={"uuid":"1","filepath":"test1.jpg"}
	Photo.create(**data)	
        
	#fake data to test get resource
	with self.app.open_resource("test_resources/photo.jpg") as fp:
            with self.client:
		response = self.client.get("/photos/v1.0/photos")
		app.logger.debug(response.json)
		app.logger.debug(response.json['data'][0]['uuid'])

    
    def test_get_photo_correct(self):
	#fake information
    	create_photo(1)   	
	#fake data to test get resource
        with self.client:
		response = self.client.get("/photos/v1.0/photos")
		app.logger.debug(response.json)
		app.logger.debug(response.json['data'][0]['uuid'])

    def test_get_photos_pagination(self):
	create_photo(102)
        with self.client:
		response = self.client.get("/photos/v1.0/photos")
		app.logger.debug(response.json)
		app.logger.debug(response.json['data'][0]['uuid'])


