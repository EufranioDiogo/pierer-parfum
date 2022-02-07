from flask_restful import Resource, fields, marshal_with, reqparse
import psycopg2

connection = None
cursor = None

origem_format = {
  'origem_pk': fields.Integer,
  'origem_name': fields.String
}

origem_args = reqparse.RequestParser()
origem_args.add_argument('origem_name', type=str, help='Need to provide origem origem_name', required=True)

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

def create_origem():
  start_connection_db()
  global cursor, connection

  args = origem_args.parse_args()
  cursor.execute(f'INSERT INTO origem(origem_name) VALUES(%s)', (args['origem_name'],))
  
  connection.commit()
  close_connection_db()

  return {
    'status': 'success',
    'message': 'origem created',
    'data': {
      'origem': args
    }
  }, 201


def get_all_origems():
  start_connection_db()
  global cursor, connection

  cursor.execute('SELECT * FROM origem')
  origems = cursor.fetchall()

  close_connection_db()

  return {
    'status': 'success',
    'message': 'origems getted',
    'data': {
      'origems': origems
    } 
  }, 200


def get_spefic_origem(origem_id = 0):
  start_connection_db()
  global cursor, connection

  cursor.execute('SELECT * FROM origem WHERE origem_pk=%s', (origem_id))

  origem = cursor.fetchone()
  
  close_connection_db()

  if (origem):
    return {
      'status': 'success',
      'message': 'origem getted',
      'data': {
        'origem': origem
      } 
    }, 200
  return {
      'status': 'success',
      'message': 'origem not getted',
      'data': {
      } 
    }, 204


def delete_origem(origem_id = 0):
  start_connection_db()
  global cursor, connection

  cursor.execute('DELETE FROM origem WHERE origem_pk=%s', (origem_id))

  connection.commit()
  
  close_connection_db()

  return {
    'status': 'success',
    'message': 'origem deleted',
    'data': {
    } 
  }, 204
