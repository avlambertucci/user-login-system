from flask import Flask, render_template

app = Flask(__name__)
from user import routes

# Routes

@app.route('/', methods=['GET', 'POST'])
def home():
  return render_template('home.html')

@app.route('/dashboard/')
def dashboard():
  return render_template('dashboard.html')