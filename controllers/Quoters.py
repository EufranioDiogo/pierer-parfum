from flask_restful import Resource, fields, marshal_with, reqparse
import psycopg2


connection = None
cursor = None

quoter_format = {
  'quoter_pk': fields.Integer,
  'name': fields.String,
  'quote': fields.String,
  'photo_url': fields.String 
}

quoter_args = reqparse.RequestParser()
quoter_args.add_argument('name', type=str, help='Need to provide quoter name', required=True)
quoter_args.add_argument('quote', type=str, help='Need to provide quote to quoter', required=True)
quoter_args.add_argument('photo_url', type=str, help='Need to provide quoter name', required=False)


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


def create_quoter():
  start_connection_db()
  global cursor, connection
  args = quoter_args.parse_args()
  
  cursor.execute(f'INSERT INTO quoter(name, quote, photo_url) VALUES(%s, %s, %s)', (args['name'], args['quote'], args["photo_url"]))
  
  connection.commit()
  close_connection_db()

  return {
    'status': 'success',
    'message': 'Quoter created',
    'data': {
      'quoter': args
    }
  }, 201
  
def get_all_quoters():
  start_connection_db()
  global cursor, connection

  cursor.execute('SELECT * FROM quoter')
  quoters = cursor.fetchall()

  close_connection_db()

  return {
    'status': 'success',
    'message': 'Quoter created',
    'data': {
      'quoters': quoters
    } 
  }, 200
  
def get_spefic_quoter(quoter_id = 0):
  start_connection_db()
  global cursor, connection

  cursor.execute('SELECT * FROM quoter WHERE quoter_pk=%s', (quoter_id))

  quoter = cursor.fetchone()
  
  close_connection_db()

  if (quoter):
    return {
      'status': 'success',
      'message': 'Quoter created',
      'data': {
        'quoter': quoter
      } 
    }, 200
  return {
      'status': 'success',
      'message': 'Quoter created',
      'data': {
      } 
    }, 204
