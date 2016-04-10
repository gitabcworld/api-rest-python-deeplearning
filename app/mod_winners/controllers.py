from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from app.mod_winners.models import Winner
from app import  app
from app.data import db
from flask.ext.login import login_required

mod_winner = Blueprint('users',__name__,url_prefix='/users')



@mod_winner.route('/home',methods=['GET','POST'])
@login_required
def home():
	app.logger.debug("Applying home")
	#TODO add order_by date
	winner = Winner.query.first()
	return render_template("users/home.html",winner=winner)
