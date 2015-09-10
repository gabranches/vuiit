from app import app
from flask import render_template
import requests
import json



@app.route('/')
def index():
	return render_template('index.html')


@app.route('/r/<sub>')
def sub_page(sub):
	return render_template('index.html', sub=str(sub))

@app.route('/link/<link>')
def link_page(link):
	return render_template('index.html', link=str(link))