from flask import render_template, Blueprint

auth = Blueprint('auth', __name__, static_folder='static', template_folder='templates')

@auth.route('/login')
def login():
  return render_template('login.html')

@auth.route('/signup')
def signup():
  return render_template('signup.html')