from flask import Flask
from flask import request
from flask import render_template
from flask import session

from ..data import db
# from ..data.user import User
# from ..data.postgres_user_dao import PostgresUserDAO

app = Flask(__name__)
app.secret_key = 'fhasdhfuy^%@456&%^#$56'
# db.connect()

# def get_user_dao():
#     return PostgresUserDAO()

# @app.route('/users')
# def users():
#     result = ""
#     for user in get_user_dao().get_users():
#         result += str(user)
#     return result    

@app.route('/')
def hello_world():
    return 'Hello, AGAIN World! How are you this evening?'

@app.route('/debugSession')
def debugSession():
    result = ''
    for key,value in session.items():
        result += key+"->"+str(value)+"<br />"
    return result

@app.route('/admin/<name>')
def greet(name):
    res = db.oneUser(name) 
    return render_template("get_user.html", username=name, passw=res[1], full=res[2])

@app.route('/admin')
def user_list():
     names = db.all_usernames() 
     return render_template("users.html", result=names)

@app.route('/admin/adduser')
def add_new_user():
    return render_template("new_user.html")

@app.route('/admin/create', methods = ['POST'])
def create_user():
    name = request.form['username']
    passwrd = request.form['password']
    fnam = request.form['fullname']
    db.insertUser(name, passwrd, fnam)
    return render_template("adduser.html")

@app.route('/admin/userinfo')
def reveal_user():
    return render_template("get_user.html", username=name)

@app.route('/admin/updateuser')
def change_user():
    return render_template("edit_user.html")

def main():
    print("python main function")

if __name__ == '__main__':
    main()
