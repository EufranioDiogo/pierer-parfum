from flask import Blueprint, render_template

homens = Blueprint('homens', __name__, static_folder='static', template_folder='templates')

@homens.route('/')
def index():
  return render_template('homens.html')