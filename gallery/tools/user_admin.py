from db import all_users

def new_user():
    userName = input("Enter a username: ")
    password = input("Enter a password: ")
    full_name = input("Enter the Full Name:")
    print("call db.insertUser with the three parameters")

def change_user():
    userName = input("Enter the username: ")
    userName2 = input("Enter the desired username: ")
    password2 = input("Enter the desired password: ")
    full_name2 = input("Enter the desired Full Name:")
    print("call db.editUser with the four parameters")

def remove_user():
    userName = input("Enter a username to be removed: ")
    print("call db.deleteUser with the three parameters")

val = 0
while val != "5":
    print("""please make a selection
    1 = List Users
    2 = Add User
    3 = Edit User
    4 = Delete User
    5 = Quit""")
    val = input("Enter Command:")
    if val == "1":
        all_users()
    elif val == "2":
        new_user()
    elif val == "3":
        change_user()
    elif val == "4":
        remove_user()


