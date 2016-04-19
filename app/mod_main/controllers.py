from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, jsonify, json
from app import app

import os


mod_main = Blueprint('main',__name__,url_prefix='/')



@mod_main.route('/',methods=['POST','GET'])
def index():
	return render_template('index.html')
