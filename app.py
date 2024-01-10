#=============================== IMPORTS ZONE ===============================
from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, IntegerField
import requests
from unidecode import unidecode
# personnal modules
import debug_sys


#=============================== INIT ZONE ===============================
app = Flask(__name__, static_url_path='',
            static_folder='templates',
            template_folder='templates')

app.secret_key = "MSI c kro bien !"

class SearchForm(FlaskForm):
    recherche = StringField('nom du pokemon', validators=[DataRequired()])

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
