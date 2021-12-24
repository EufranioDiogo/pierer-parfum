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

family_format = {
  'family_pk': fields.Integer,
  'family_name': fields.String
}

family_args = reqparse.RequestParser()
family_args.add_argument('family_name', type=str, help='Need to provide family family_name', required=True)


def create_family():
  start_connection_db()
  global cursor, connection

  args = family_args.parse_args()
  cursor.execute(f'INSERT INTO family(family_name) VALUES(%s)', (args['family_name'],))
  
  connection.commit()
  close_connection_db()

  return {
    'status': 'success',
    'message': 'family created',
    'data': {
      'family': args
    }
  }, 201
  
def get_all_families():
  start_connection_db()
  global cursor, connection

  cursor.execute('SELECT * FROM family')
  familys = cursor.fetchall()

  close_connection_db()

  return {
    'status': 'success',
    'message': 'familys getted',
    'data': {
      'familys': familys
    } 
  }, 200

def get_spefic_family(family_id = 0):
  start_connection_db()
  global cursor, connection

  cursor.execute('SELECT * FROM family WHERE family_pk=%s', (family_id))

  family = cursor.fetchone()
  
  close_connection_db()

  if (family):
    return {
      'status': 'success',
      'message': 'family getted',
      'data': {
        'family': family
      } 
    }, 200
  return {
      'status': 'success',
      'message': 'family not getted',
      'data': {
      } 
    }, 204

def delete_family(family_id = 0):
  start_connection_db()
  global cursor, connection

  cursor.execute('DELETE FROM family WHERE family_pk=%s', (family_id))

  connection.commit()
  
  close_connection_db()

  return {
    'status': 'success',
    'message': 'family deleted',
    'data': {
    } 
  }, 204