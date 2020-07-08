from . import db
from .photo import Photo
from .photo_dao import PhotoDAO 

class PostgresPhotoDAO(PhotoDAO):
    def __init__(self):
        pass

    def get_photos_by_username(self, username):
        result = []
        cursor = db.execute("select title, username from photos where username=%s;", (username,))
        for t in cursor.fetchall():
            result.append(Photo(t[0], t[1]))
        return result
    
    def add_photo(self, photo):
        query = "insert into photos (title, username) values(%s, %s);"
        try:
            return db.execute(query, (photo.title, photo.username))
        except:
            print("Unexpected error: ")

    