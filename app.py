from flask import Flask, render_template, redirect, session
from functools import wraps
import pymongo
from extensions import mongo

app = Flask(__name__)
app.secret_key = b'\xc6\xb2\x95\x18>P\xa5C\xaa\x99s\xad{D\x01\x94'
#Database
app.config['MONGO_URI'] = 'mongodb+srv://admin:182182@cluster0.cxaae.mongodb.net/user_list?retryWrites=true&w=majority'
mongo.init_app(app)
users_collection = mongo.db.user_list
#Decorators
def login_required(f):
  @wraps(f)
  def wrap(*args, **kwargs):
    if 'logged_in' in session:
      return f(*args, **kwargs)
    else:
      return redirect('/')
  return wrap


from user import routes

# Routes

@app.route('/', methods=['GET', 'POST'])
def home():
  return render_template('home.html')

@app.route('/dashboard/')
@login_required
def dashboard():
  return render_template('dashboard.html')