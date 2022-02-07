from flask import Blueprint, render_template

mulheres = Blueprint('mulheres', __name__, static_folder='static', template_folder='templates')

@mulheres.route('/')
def index():
  return render_template('mulheres.html')