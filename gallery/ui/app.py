from flask import Flask
from flask import request
from flask import render_template
from flask import session
from flask import redirect
from flask import flash
from flask import url_for

import os
from werkzeug.utils import secure_filename
from functools import wraps

from ..data.photos import add_photo
from ..data.photos import get_photos
from ..data import db
from ..data.user import User
from ..data.postgres_user_dao import PostgresUserDAO
from ..aws.s3 import put_object

bucket = os.getenv("S3_IMAGE_BUCKET")
UPLOAD_FOLDER = bucket
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.secret_key = 'fhasdhfuy^%@456&%^#$56'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db.connect()

def check_admin():
    return 'username' in session and (session['username'] == 'Matt' or session['username'] == 'dongji')

def requires_admin(view):
    @wraps(view)
    def decorated(**kwargs):
        if not check_admin():
            return redirect('/login')
        return view(**kwargs)
    return decorated

def get_user_dao():
    return PostgresUserDAO()


@app.route('/admin/users')
@requires_admin
def users():
    return render_template('users.html', users=get_user_dao().get_users())

@app.route('/admin/deleteUser/<username>')
@requires_admin
def deleteUser(username):
    db.connect()
    return render_template('deluser.html', title="Confirm delete",
                                            message="Are you sure you want to delete this user",
                                            on_yes="/admin/executeDeleteUser/"+username,
                                            on_no="/admin/users")

@app.route('/admin/executeDeleteUser/<username>')
@requires_admin
def executeDeleteUser(username):
    db.connect()
    get_user_dao().delete_user(username)
    return redirect('/admin/users')
    
@app.route('/')
def main_menu():
    if session['username'] is None:
        return render_template('mainMenu.html', user='.... you are not logged in after all.')
    else:
        return render_template('mainMenu.html', user=session['username'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/uploadImage/<username>', methods=['GET', 'POST'])
def upload_file(username):
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            if put_object(bucket, file.filename, file):
                db.add_photo(file.filename, username)
            return redirect('/')
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    <a href="../">Home</a>
    '''


@app.route('/viewImages/<username>')
def viewImages(username):
    pics = get_photos(bucket, username)
    if not pics:
        return 'No Photos Present for you...' 
    return render_template('photos.html', title='Image Gallery',user=username,photos=get_photos(bucket, username))

@app.route('/invalidLogin')
def invalidLogin():
    return 'Invalid Login'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = get_user_dao().get_user_by_username(request.form['username']) 
        if user is None or user.password != request.form['password']:
            return redirect('/invalidLogin')
        else: 
            session['username'] = request.form['username']
            return redirect('/')    
    else:
        return render_template('login.html')

@app.route('/debugSession')
def debugSession():
    result = ''
    for key,value in session.items():
        result += key+"->"+str(value)+"<br />"
    return result

@app.route('/admin/<name>')
@requires_admin
def greet(name):
    res = db.oneUser(name) 
    return render_template("users.html", username=name, passw=res[1], full=res[2])


@app.route('/admin/adduser')
@requires_admin
def add_new_user():
    return render_template("new_user.html")

@app.route('/admin/create', methods = ['POST'])
@requires_admin
def create_user():
    name = request.form['username']
    passwrd = request.form['password']
    fnam = request.form['fullname']
    db.insertUser(name, passwrd, fnam)
    return render_template("adduser.html")

@app.route('/admin/userinfo')
@requires_admin
def reveal_user():
    return render_template("get_user.html", username=name)

@app.route('/admin/updateuser')
@requires_admin
def change_user():
    return render_template("edit_user.html")

def main():
    print("python main function")

if __name__ == '__main__':
    main()
