from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from werkzeug import check_password_hash, generate_password_hash
from app import app
from app.data import db

from app.mod_photos.models import Photo

mod_photos = Blueprint('photos',__name__,url_prefix='/photos')


@mod_photos('/photos/',methods=['POST'])
def photos():
	app.logger.debug("Applying post photo...")
	

'''
def check_password(pass1 , pass2):
    return pass1 == pass2
    
@mod_auth.route('/signin/',methods=['GET','POST'])
def signin():
    app.logger.debug("Applying Signin")
    form = LoginForm(request.form)
    if form.validate_on_submit():
        app.logger.debug("It was validated user information to signin")
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password(user.password,form.password.data):
            session['user_id']= user.id
            app.logger.debug('Logged user=%s',user.name)
	    #Logged user
	    login_user(user)
	    return redirect(url_for('users.home'))
	    #return render_template('users/home.html',winner=user)
        flash('Wrong email or password', 'error-message')
    return render_template("auth/signin.html",form=form)

@mod_auth.route('/register/',methods=['GET','POST'])
def register():
    app.logger.debug("Applying register")
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        app.logger.debug("It was validated user information for registering")
        user = User.query.filter_by(email=form.email.data).first()
	if user:
            app.logger.debug('This user exists')
            flash('This user exists','error-message')
	    return render_template(url_for('auth/register.html',form=form))
        User.create(**form.data)
        app.logger.debug("User registered sucessfully")
        flash("The user was registered successful")

    return render_template("auth/register.html",form=form)
'''
