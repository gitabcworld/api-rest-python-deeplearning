from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, jsonify, json
from werkzeug import check_password_hash, generate_password_hash
from app import app
from app.data import db
from app.mod_photos.models import Photo

from factory_responses import FactoryResponse

import uuid
import os

ALLOWED_EXTENSIONS=set(['jpg','jpeg','bmp','png'])

mod_photos = Blueprint('photos',__name__,url_prefix='/photos/v1.0')


responses = FactoryResponse()

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS


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
		f_name=str(uuid.uuid4()) + extension
		app.logger.debug("f_name="+f_name)
		filepath=os.path.join(app.config['UPLOAD_FOLDER'], f_name)
		photo = Photo(f_name,filepath)
		data ={'uuid':f_name, 'filepath': filepath}
		Photo.create(**data)
		file.save(filepath)
                data = {'filename':f_name}
        #TODO refactor to set up necessary methods to create responses
        #TODO is it necessary to return 200 command
	resp = None
	if data == None:
        	resp = responses.new200()
	else:
		resp = responses.new201(data)
        return resp

@mod_photos.route('/photos/<int:id>',methods=['GET'])
def get_photos_one(id):
    photo =Photo.query.get_or_404(id)
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

