from flask_restful import Resource, fields, marshal_with, reqparse
import psycopg2

connection = None
cursor = None

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

product_format = {
  'product_pk': fields.Integer,
  'name': fields.String,
  'price': fields.Float,
  'origem_fk': fields.Integer,
  'family_fk': fields.Integer,
  'fragance_rate': fields.Integer,
  'gender': fields.String,
}

product_args = reqparse.RequestParser()
product_args.add_argument('name', type=str, help='Need to provide product name', required=True)
product_args.add_argument('price', type=float, help='Need to provide price to product', required=True)
product_args.add_argument('origem_fk', type=int, help='Need to provide origem_fk to product', required=True)
product_args.add_argument('family_fk', type=int, help='Need to provide family_fk to product', required=True)
product_args.add_argument('fragance_rate', type=int, help='Need to provide fragance rate to product', required=True)
product_args.add_argument('gender', type=str, help='Need to provide gender to product', required=True)


def create_product():
  start_connection_db()
  global cursor, connection

  args = product_args.parse_args()
  cursor.execute(f'INSERT INTO product(name, price, origem_fk, family_fk, fragance_rate, gender) VALUES(%s, %s, %s)', (args['name'], args['price'], args["origem_fk"], args["family_fk"], args["fragance_rate"], str(args["gender"]).lower()[0]))
  
  connection.commit()
  close_connection_db()

  return {
    'status': 'success',
    'message': 'product created',
    'data': {
      'product': args
    }
  }, 201
  
def get_all_products():
  start_connection_db()
  global cursor, connection

  cursor.execute('SELECT * FROM product')
  products = cursor.fetchall()

  close_connection_db()

  return {
    'status': 'success',
    'message': 'product created',
    'data': {
      'products': products
    } 
  }, 200

def get_all_female_products():
  start_connection_db()
  global cursor, connection

  cursor.execute('SELECT * FROM product WHERE gender=%s', ('f'))
  products = cursor.fetchall()

  close_connection_db()

  return {
    'status': 'success',
    'message': 'product created',
    'data': {
      'products': products
    } 
  }, 200

def get_all_male_products():
  start_connection_db()
  global cursor, connection

  cursor.execute('SELECT * FROM product WHERE gender=%s', ('m'))
  products = cursor.fetchall()

  close_connection_db()

  return {
    'status': 'success',
    'message': 'product created',
    'data': {
      'products': products
    } 
  }, 200
  
def get_spefic_product(product_id = 0):
  start_connection_db()
  global cursor, connection

  cursor.execute('SELECT * FROM product WHERE product_pk=%s', (product_id))

  product = cursor.fetchone()
  
  close_connection_db()

  if (product):
    return {
      'status': 'success',
      'message': 'product created',
      'data': {
        'product': product
      } 
    }, 200
  return {
      'status': 'success',
      'message': 'product created',
      'data': {
      } 
    }, 204

def delete_product(product_id = 0):
  start_connection_db()
  global cursor, connection

  cursor.execute('DELETE FROM product WHERE product_pk=%s', (product_id))

  connection.commit()
  
  close_connection_db()

  return {
    'status': 'success',
    'message': 'product created',
    'data': {
    } 
  }, 204