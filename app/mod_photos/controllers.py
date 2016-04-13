from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, jsonify, json
from werkzeug import check_password_hash, generate_password_hash
from app import app
from app.data import db
from app.mod_photos.models import Photo

import uuid
import os

mod_photos = Blueprint('photos',__name__,url_prefix='/photos/v1.0')



@mod_photos.route('/photos',methods=['POST'])
def photos():
	app.logger.debug("Applying post photo...")

        data = None
        if request.method == 'POST':
		file = request.files['file']
		extension = os.path.splitext(file.filename)[1]
		f_name=str(uuid.uuid4()) + extension
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], f_name))
                data = {'filename':f_name}
        #TODO refactor to set up necessary methods to create responses
        if data == None:
            resp = jsonify()
        else:
            resp = jsonify(data)
        resp.status_code == 200
        return resp

