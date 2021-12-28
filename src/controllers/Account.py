from flask_restful import Resource, fields, marshal_with, reqparse
import psycopg2
import bcrypt
from jwt import encode

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
  return bcrypt.checkpw(plain_text_password, hashed_password)

def create_account():
  global cursor, connection
  start_connection_db()
  args = account_args.parse_args()
  args['password'] = args['password'].encode('utf-8')
  passwordEncrypted = get_hashed_password(args['password'])
  
  try:
      cursor.execute(f'INSERT INTO account(username, email, password) VALUES(%s, %s, %s)', (args['username'], args['email'], passwordEncrypted,))
  
      connection.commit()
      close_connection_db()


      jwt_token = encode({ 'data': f'{args["username"]} {passwordEncrypted}' }, 'EXAMPLE',algorithm='HS256')
      

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
  print(username)
  password = args['password'].encode('utf-8')


  cursor.execute('SELECT username, password FROM account WHERE username=%s', (username,))

  user = cursor.fetchone()
  close_connection_db()

  if (user):
    if check_password(password, user[1].encode('utf-8')):
      jwt_token = encode({'data': f'{args["username"]} {user[1]}' }, 'EXAMPLE',algorithm='HS256')

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