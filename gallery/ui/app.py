from flask import Flask
from flask import request
from flask import render_template

from db import all_users
from db import all_usernames
from db import insertUser
from db import editUser
from db import deleteUser
from db import oneUser

app = Flask(__name__)

@app.route('/')
def hello_world():
    y = 1
    return 'Hello, AGAIN World!, how are you this evening?'

@app.route('/goodbye')
def goodbye():
    return 'Goodbye'

@app.route('/admin/<name>')
def greet(name):
    res = oneUser(name) 
    return render_template("get_user.html", username=name, passw=res[1], full=res[2])
# fname=res[1])


@app.route('/admin')
def user_list():
     names = all_usernames() 
     return render_template("users.html", result=names)

@app.route('/admin/adduser')
def add_new_user():
    return render_template("new_user.html")

@app.route('/admin/create', methods = ['POST'])
def create_user():
    name = request.form['username']
    passwrd = request.form['password']
    fnam = request.form['fullname']
    insertUser(name, passwrd, fnam)
    return render_template("adduser.html")


@app.route('/admin/userinfo')
def reveal_user():
    return render_template("get_user.html", username=name)

@app.route('/admin/updateuser')
def change_user():
    return render_template("edit_user.html")