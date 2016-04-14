from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, jsonify, json
from werkzeug import check_password_hash, generate_password_hash
from app import app
from app.data import db
from app.mod_photos.models import Photo

import uuid
import os

ALLOWED_EXTENSIONS=set(['jpg','jpeg','bmp','png'])

mod_photos = Blueprint('photos',__name__,url_prefix='/photos/v1.0')

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS


@mod_photos.route('/photos',methods=['POST'])
def photos():
	app.logger.debug("Applying post photo...")

        data = None
        if request.method == 'POST':
		file = request.files['file']
		if file and not allowed_file(file.filename):
            	    resp = jsonify()
        	    resp.content_type='application/json'
    		    resp.status_code = 202
		    return resp

		extension = os.path.splitext(file.filename)[1]
		f_name=str(uuid.uuid4()) + extension
		filepath=os.path.join(app.config['UPLOAD_FOLDER'], f_name)
		photo = Photo(f_name,filepath)
		data ={'uuid':f_name, 'filepath': filepath}
		Photo.create(**data)
		file.save(filepath)
                data = {'filename':f_name}
        #TODO refactor to set up necessary methods to create responses
        if data == None:
            resp = jsonify()
            resp.status_code = 200
        else:
            resp = jsonify(data)
	    resp.status_code = 201
	#TODO add diferent type of constructors
        resp.content_type='application/json'
        return resp

