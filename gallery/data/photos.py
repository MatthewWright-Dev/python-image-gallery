from .db import execute
from ..aws.s3 import get_object

def add_photo(title, username):
	query = "insert into photos (title, username) values(%s, %s);"
	try:
		return execute(query, (title, username))
	except:
		print("Unexpected error: ")

def get_photos(bucket_name, username):
    result = []
    cursor = execute("select title, username from photos where username=%s;", (username,))
    for t in cursor.fetchall():
        result.append(get_object(bucket_name, t[0]))
    return result