from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, jsonify, json
from werkzeug import check_password_hash, generate_password_hash
from app import app
from app.data import db
from app.mod_photos.models import Photo

from factory_responses import FactoryResponse
from subprocess import check_output

import uuid
import os
import base64

ALLOWED_EXTENSIONS=set(['jpg','jpeg','bmp','png','JPG','JPEG','BMP','PNG'])

mod_photos = Blueprint('photos',__name__,url_prefix='/photos/v1.0')

responses = FactoryResponse()

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS

def timestamp():
	import time
	return str(time.time()).split(".")[0]

@mod_photos.route('/photos',methods=['POST'])
def post_photos():
	app.logger.debug("Applying post photo...")

	data = None
	if request.method == 'POST':
		app.logger.debug("Applying post image")
		file = request.files['file']

		#TODO pending for testing!
		#if file and not allowed_file(file.filename):
		#    return responses.new202()

		extension = os.path.splitext(file.filename)[1]
		identifier=timestamp()+str(uuid.uuid4())
		f_name=identifier + extension
		app.logger.debug("f_name="+f_name)
		app.logger.debug("identifier="+identifier)
		filepath=os.path.join(app.config['UPLOAD_FOLDER'], f_name)
		#First result

		data_to_object ={'uuid':identifier, 'filepath': filepath, 'analysed':False, 'info':str("empty")}
		new_photo = Photo.create(**data_to_object)

		data = {'filename':new_photo.filepath, 'uuid': new_photo.uuid}
        #TODO refactor to set up necessary methods to create responses
        #TODO is it necessary to return 200 command
	resp = None
	if data == None:
        	resp = responses.new200()
	else:
		resp = responses.new201(data)
	return resp

@mod_photos.route('/photoStr',methods=['POST'])
def post_photosStr():
	app.logger.debug("Applying post photo...")

	data = None
	if request.method == 'POST':

		content = request.get_json()
		if content is not None:
			filename = content['filename']
			extension = os.path.splitext(filename)[1]

			imageEncoded = content['image']
			image = base64.b64decode(imageEncoded)
			#image = image.decode('base64')

			app.logger.debug(data)
			identifier=timestamp()+str(uuid.uuid4())

			f_name=identifier + extension
			app.logger.debug("f_name="+f_name)
			app.logger.debug("identifier="+identifier)
			filepath=os.path.join(app.config['UPLOAD_FOLDER'], f_name)
			# or, more concisely using with statement
			with open(filepath, "wb") as fh:
	    			fh.write(image)
			#First result

			data_to_object ={'uuid':identifier, 'filepath': filepath, 'analysed':False, 'info':str("empty")}
			new_photo = Photo.create(**data_to_object)

			data = {'uuid': new_photo.uuid }
        	#TODO refactor to set up necessary methods to create responses
        	#TODO is it necessary to return 200 command
	resp = None
	if data == None:
        	resp = responses.new200()
	else:
		resp = responses.new201(data)
	return resp


@mod_photos.route('/photos/<string:uuid>',methods=['GET'])
def get_photos_one(uuid):
	#photo =Photo.query.get_or_404(id)
	photo = Photo.query.filter_by(uuid=uuid).first_or_404()
	return jsonify(photo.serialize_all())

@mod_photos.route('/photos',methods=['GET'])
def get_photos():
	app.logger.debug("Applying get photos...")
	photos = Photo.query.all()
	page = request.args.get('page',1,type=int)
	pagination=Photo.query.paginate(page,per_page=app.config['PER_PAGE'],
                error_out=False)
        photos = pagination.items
        prev = None
        if pagination.has_prev:
            prev=url_for('photos.get_photos',page=page-1,_external=True)
        next = None
        if pagination.has_next:
            next = url_for('photos.get_photos',page=page+1,_external=True)

	resp = jsonify({'data' :[photo.serialize() for photo in photos],
            'pagination':{'prev': prev,'next': next,'count':pagination.total}
            })
	return resp
