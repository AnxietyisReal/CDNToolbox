import os
import boto
import boto.s3.connection

if (os.environ.get('ACCESS_KEY') == None and os.environ.get('SECRET_KEY') == None and os.environ.get('OBJHOST') == None):
  print('Please set ACCESS_KEY, SECRET_KEY and OBJHOST in your environment variables.')
  exit()

conn = boto.connect_s3(
  aws_access_key_id=os.environ.get('ACCESS_KEY'),
  aws_secret_access_key=os.environ.get('SECRET_KEY'),
  host = os.environ.get('OBJHOST'),
  calling_format = boto.s3.connection.OrdinaryCallingFormat(),
)

domain = 'https://cdn.toast-server.net/'
bucket = conn.get_bucket('cdn.toast-server.net')
filename = ''
obj_filename = ''
