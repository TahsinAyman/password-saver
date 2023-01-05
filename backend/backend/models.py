import sqlite3
from . import sql
import json

x = sqlite3.connect("password.db")
c = x.cursor()
table = "passwords"
f = sql.Fetch(c,table=table,row_id=True)
a = sql.Add(c,table=table)
u = sql.Update(c,table=table)

def merge(x:dict, y:dict) :
    x.update(y)
    return x



def fetch_content(username):
    main_id = f.get_spec_commponent_str(component="username",string = username)
    return main_id[0][3]



def authenticate(username, password) -> bool:
    # if f.get_spec_commponent_str(component="username",string=username):
    x = f.get_spec_commponent_str(component="username",string=username) 

    if x:
        if x[0][2] == password:
            return True
    return False


def create_user(username,password) ->  bool:
    if not authenticate(username=username, password=password):
        a.insert_one([username,password,"{}"])
        return True
    return False    


def add_content(username, content):
    cont = str(merge(eval(fetch_content(username=username)), eval(content)))
    u.update_records_str(component='content',string =cont, condition = f" username = '{username}' ")
    return fetch_content(username=username)





    # rowid, username, auth_password, content
    # Epic Backend Developer

def give_all():
    return f.get_all()


# print(add_content(username="Ishaan",content="{}"))

# print(authenticate(username="Ishaan", password = "12345"))

# sql.create(c,table = table, username = "text",auth_password = "text",content = "text")