from flask import Blueprint, render_template

myBuyOrders = Blueprint('myBuyOrders', __name__, static_folder='static', template_folder='templates')

@myBuyOrders.route('/')
def index():
  return render_template('myBuyOrders.html')