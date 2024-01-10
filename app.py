#=============================== IMPORTS ZONE ===============================
from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, IntegerField
import requests
from random import random
from unidecode import unidecode
# personnal modules
import debug_sys


#=============================== INIT ZONE ===============================
app = Flask(__name__, static_url_path='',
            static_folder='public',
            template_folder='templates')

app.secret_key = str(round(random(),2)for _ in range(10))


if __name__ == '__main__':
    app.run(debug=True)

#=============================== MAIN ZONE ===============================
@app.route('/')
def index():
    debug_sys.log('INFO','connection : index')
    return render_template('index.html')

@app.route('/blog')
def blog():
    debug_sys.log('INFO','connection : blog')
    return render_template('Blog.html')
