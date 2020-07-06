import psycopg2
import json
from ..aws import secrets
#from secrets import get_secret_image_gallery

db_host = "image-gallery.cgh7vkgen2ke.us-east-2.rds.amazonaws.com"
db_name="image_gallery"
db_user="image_gallery"


connection = None

def get_secret():
        jsonString = secrets.get_secret_image_gallery()
        return json.loads(jsonString)

def get_password(secret):
        return secret['password']

def connect():
	global connection
	secret = get_secret()
	connection = psycopg2.connect(host=db_host, dbname=db_name, user=db_user, password=get_password(secret))
	connection.set_session(autocommit=True)

def execute(query, args=None):
	global connection
	cursor = connection.cursor()
	if not args :
               	cursor.execute(query)
	else:
		cursor.execute(query, args)
	return cursor

def all_users():
	connect()
	res = execute('select * from users')
	for row in res:
		print(row)

def all_usernames():
	connect()
	res = execute('select username from users')
	arr = []
	for row in res:
		a = str(row).replace(')', '')
		a = a.replace('(','')
		a = a.replace(',','')
		a = a.replace('\'', '')
		arr.append(a)
	return arr

def insertUser(userName, password, full_name):
	connect()
	query = "insert into users (userName, password, full_name) values(%s, %s, %s);"
	try:
		return execute(query, (userName, password, full_name))
	except:
		print("Unexpected error: ")

def deleteUser(userName):
	connect()
	query = "DELETE FROM users WHERE username=%s;"
	try:
		execute(query, (userName,))
	except Exception as e:
		print("Unexpected error", e)

def oneUser(name):
	connect()
	query = "select * from users where username=%s;"
	res = execute(query, (name,))
	arr = []
	for row in res:
		arr.append(row)
	a = []
	for item in arr:
		a.extend(item)	
	# for row in res:
	# 	a = str(row).replace(')', '')
	# 	a = a.replace('(','')
	# 	a = a.replace(',','')
	# 	a = a.replace('\'', '')
	# 	arr.append(a)
	# ar = [i[0] for i in arr]
	return a

def editUser(userName, userName2, password2, full_name2):
	connect()
	deleteUser(userName)
	query = "insert into users (userName, password, full_name) values(%s, %s, %s);"
	try:
		execute(query, (userName2, password2, full_name2))
	except:
		print("Unexpected error")
