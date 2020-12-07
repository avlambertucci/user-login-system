from flask import Flask, render_template
import pymongo
from extensions import mongo

app = Flask(__name__)
#Database
app.config['MONGO_URI'] = 'mongodb+srv://admin:182182@cluster0.cxaae.mongodb.net/user_list?retryWrites=true&w=majority'
mongo.init_app(app)
users_collection = mongo.db.user_list
# client = pymongo.MongoClient('localhost', 27017)
# db = client.user_login_system
from user import routes

# Routes

@app.route('/', methods=['GET', 'POST'])
def home():
  return render_template('home.html')

@app.route('/dashboard/')
def dashboard():
  return render_template('dashboard.html')