from flask_restful import fields, marshal_with, reqparse, request
from pexpect import ExceptionPexpect
import psycopg2
from jwt import encode, decode, utils
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
  token = str(request.headers.get('Authorization'))[1:]
  token = token[:len(token) - 1]
  token_information = decode(token, key='mjnsdjnsjddsjdns')
  
  cursor.execute('SELECT account_pk, username, password FROM account WHERE username=%s', (token_information['username'],))

  user = cursor.fetchone()

  try:
      cursor.execute('INSERT INTO buy_orders(product_fk, account_fk, quant_products, price_per_product, total_price, date) VALUES (%s, %s, %s, %s, %s, %s);', (args['product_fk'], user[0], args['quant_product'], args['price_per_product'], args['total_price'], args['date']))
      
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


def get_my_buy_orders():
  global cursor, connection
  start_connection_db()


  token = str(request.headers.get('Authorization'))[1:]
  token = token[:len(token) - 1]
  token_information = decode(token, key='mjnsdjnsjddsjdns')
  
  cursor.execute('SELECT account_pk, username, password FROM account WHERE username=%s', (token_information['username'],))

  user = cursor.fetchone()

  cursor.execute('SELECT P.product_pk, P.name, O.origem_name, F.family_name, P.fragance_rate, P.gender, P.price, P.product_photo  FROM buy_orders B, product P, family F, origem O WHERE P.product_pk = B.product_fk AND B.account_fk = %s AND F.family_pk = P.family_fk AND O.origem_pk = P.origem_fk', (user[0],))

  my_buy_orders = cursor.fetchall()
  
  close_connection_db()

  try:
      return {
        'status': 'success',
        'message': 'buy order created',
        'data': {
          'products': my_buy_orders
          } 
        }, 200
  except print(0):
      return {
        'status': 'insucess',
        'message': 'buy order not created',
        'data': {
        } 
      }, 500
