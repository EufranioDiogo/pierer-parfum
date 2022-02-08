from flask_restful import fields, marshal_with, reqparse, request
from pexpect import ExceptionPexpect
import psycopg2
from jwt import encode, decode
connection = None
cursor = None



buy_format = {
  'product_fk': fields.Integer,
  'account_fk': fields.Integer,
  'quant_products': fields.Integer,
  'price_per_product': fields.Float,
  'total_price': fields.Float,
  'date': fields.DateTime,
}

buy_args = reqparse.RequestParser()
buy_args.add_argument('product_fk', type=int, help='Need to provide product_fk to buy order', required=True)
buy_args.add_argument('account_fk', type=int, help='Need to provide account_fk to buy order', required=True)
buy_args.add_argument('quant_product', type=int, help='Need to provide quant_products to buy order', required=True)
buy_args.add_argument('price_per_product', type=float, help='Need to provide price_per_product to buy order', required=True)
buy_args.add_argument('total_price', type=float, help='Need to provide total_price to buy order', required=True)
buy_args.add_argument('date', help='Need to provide date of buy order', required=True)

def start_connection_db():
  global connection 
  connection = psycopg2.connect(
    host='localhost',
    database='sm_db',
    user='postgres',
    password='postgres'
  )

  global cursor 
  cursor = connection.cursor()

def close_connection_db():
  global connection 
  global cursor 
  cursor.close()
  connection.close()
  
def post_buy_spefic_product(product_id = 0):
  start_connection_db()
  global cursor, connection

  args = buy_args.parse_args()
  
  if product_id != args['product_fk']:
    return {
        'status': 'insucess',
        'message': 'buy order not created, not the same product id',
        'data': {
        } 
      }, 400
  print(str(request.headers.get('Authorization')))

  try:
      cursor.execute('INSERT INTO buy_orders(product_fk, account_fk, quant_products, price_per_product, total_price, date) VALUES (%s, %s, %s, %s, %s, %s);', (args['product_fk'], args['account_fk'], args['quant_product'], args['price_per_product'], args['total_price'], args['date']))
      
      connection.commit()
      close_connection_db()
      return {
        'status': 'success',
        'message': 'buy order created',
        'data': {
          } 
        }, 200
  except print(0):
      return {
        'status': 'insucess',
        'message': 'buy order not created',
        'data': {
        } 
      }, 500

