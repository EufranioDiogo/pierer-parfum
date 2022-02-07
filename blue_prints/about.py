from flask import Blueprint, render_template

about = Blueprint('about', __name__, static_folder='static', template_folder='templates')

@about.route('/')
def index():
  return render_template('about.html')