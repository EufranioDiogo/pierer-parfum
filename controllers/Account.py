from flask_restful import fields, request, reqparse
import psycopg2
import bcrypt
from jwt import encode, decode

connection = None
cursor = None

account_format = {
  'account_pk': fields.Integer,
  'username': fields.String,
  'email': fields.String,
  'password': fields.String 
}

account_args = reqparse.RequestParser()
account_args.add_argument('username', type=str, help='Need to provide username', required=True)
account_args.add_argument('email', type=str, help='Need to provide email to account')
account_args.add_argument('password', type=str, help='Need to provide password name', required=False)


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

def get_hashed_password(plain_text_password):
  return bcrypt.hashpw(plain_text_password, bcrypt.gensalt())

def check_password(plain_text_password, hashed_password):
  return bcrypt.checkpw(plain_text_password, hashed_password, salt=bcrypt.gensalt())

def create_account():
  global cursor, connection
  start_connection_db()
  args = account_args.parse_args()
  password = args['password'] 
  args['password'] = args['password'].encode('utf-8')
  passwordEncrypted = get_hashed_password(args['password'])
  
  try:
      cursor.execute(f'INSERT INTO account(username, email, password) VALUES(%s, %s, %s)', (args['username'], args['email'], password,))
  
      connection.commit()
      close_connection_db()
      payload = {
        'username': args['username']
      }
      jwt_token = encode(payload=payload, key="mjnsdjnsjddsjdns")
      

      return {
        'status': 'success',
        'message': 'Account created',
        'data': {
          'token': jwt_token
        }
      }, 201
  except print(0):
      return {
        'status': 'not success',
        'message': 'Account not created',
        'data': {
        }
      }, 500

def account_verification():
  global cursor, connection
  start_connection_db()
  args = account_args.parse_args()
  username = args['username']
  password = args['password'].encode('utf-8')


  cursor.execute('SELECT username, password FROM account WHERE username=%s', (username,))

  user = cursor.fetchone()
  close_connection_db()
  print(user[1])


  if (user):
    if user[1] == args['password']:
      payload = {
        'username': args['username']
      }
      jwt_token = encode(payload=payload, key="mjnsdjnsjddsjdns")

      return {
        'status': 'success',
        'message': 'Account verified',
        'data': {
          'token': jwt_token
        }
      }, 200

  return {
    'status': 'no success',
    'message': 'Account not verified',
    'data': {
    }
  }, 403
  

def verify_authenticity():
  global cursor, connection
  start_connection_db()


  token = str(request.headers.get('Authorization'))[1:]
  token = token[:len(token) - 1]
  token_information = decode(token, key='mjnsdjnsjddsjdns')
  
  cursor.execute('SELECT account_pk, username, password FROM account WHERE username=%s', (token_information['username'],))

  user = cursor.fetchone()
  close_connection_db()


  if (user):
    return {
      'status': 'success',
      'message': 'Account verified',
      'data': {
      }
    }, 200
  return {
    'status': 'no success',
    'message': 'Account not verified',
    'data': {
    }
  }, 403