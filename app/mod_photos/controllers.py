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

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS


@mod_photos.route('/photos',methods=['POST'])
def photos():
	responses = FactoryResponse()
	app.logger.debug("Applying post photo...")

        data = None
        if request.method == 'POST':
		file = request.files['file']
		if file and not allowed_file(file.filename):
		    return responses.new202()

		extension = os.path.splitext(file.filename)[1]
		f_name=str(uuid.uuid4()) + extension
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

