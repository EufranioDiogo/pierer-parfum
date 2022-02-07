from flask import Blueprint, render_template

buy = Blueprint('buy', __name__, static_folder='static', template_folder='templates')

@buy.route('/')
def index():
  return render_template('buy-product.html')