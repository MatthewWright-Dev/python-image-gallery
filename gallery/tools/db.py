import psycopg2

db_host ="database-1.cgh7vkgen2ke.us-east-2.rds.amazonaws.com"
db_name="image_gallery"
db_user="image_gallery"

password_file = "/home/ec2-user/.image_gallery_config"

connection = None

def get_password():
        f = open(password_file, "r")
        result = f.readline()
        f.close()
        return result[:-1]

def connect():
	global connection
	connection = psycopg2.connect(host=db_host, dbname=db_name, user=db_user, password=get_password())
	connection.set_session(autocommit=True)

def execute(query, args=None):
	global connection
	cursor = connection.cursor()
	if not args :
               	cursor.execute(query)
	else:
		cursor.execute(query, args)
	return cursor

#def main():
def all_users():
	connect()
	res = execute('select * from users')
	for row in res:
		print(row)
#	res = execute("update users set password=%s where username='fred'", ('banana',))
#	res = execute('select * from users')
#	for row in res:
#		print(row)

#if __name__ == '__main__':
#        main()
def insertUser(userName, password, full_name):
	connect()
	query = "insert into users (userName, password, full_name) values(%s, %s, %s);"
	try:
		execute(query, (userName, password, full_name))
	except:
		print("Unexpected error: ")

def deleteUser(userName):
	connect()
	query = "DELETE FROM users WHERE username=%s;"
	try:
		execute(query, (userName,))
	except Exception as e:
		print("Unexpected error", e)

def editUser(userName, userName2, password2, full_name2):
	connect()
	deleteUser(userName)
	query = "insert into users (userName, password, full_name) values(%s, %s, %s);"
	try:
		execute(query, (userName2, password2, full_name2))
	except:
		print("Unexpected error")
