from flask import Flask
from flask import request
from flask import render_template

from db import all_users
from db import all_usernames
from db import insertUser
from db import editUser
from db import deleteUser


app = Flask(__name__)

@app.route('/')
def hello_world():
    y = 1
    return 'Hello, AGAIN World!, how are you this evening?'

@app.route('/goodbye')
def goodbye():
    return 'Goodbye'

@app.route('/greet/<name>')
def greet(name):
    return 'nice to meet you ' + name


@app.route('/admin')
def user_list():
     name1 = 'testies'
     names = all_usernames() 
     return render_template("users.html", name=names[0])

@app.route('/admin/adduser')
def add_new_user():
    return render_template("new_user.html")
