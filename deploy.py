from flask import Flask
from flask import jsonify
from flask import render_template
import MySQLdb
import mysql.connector
from mysql.connector import connection
from database import *


app = Flask(__name__)
cnx = connection.MySQLConnection(user='root',
                                 password='se2018',
                                 host='127.0.0.1',
                                 database='se_proj')
c = sql_conn(cnx)


@app.route("/")
def index_void():
    return render_template('index.html')


@app.route("/index.html")
def index():
    return render_template('index.html')


@app.route("/login.html")
def login():
    return render_template('login.html')


@app.route("/mainpage.html")
def mainpage():
    return render_template('mainpage.html')


@app.route("/imagelabel.html")
def imagelabel():
    return render_template('imagelabel.html')


@app.route("/publish.html")
def publish():
    return render_template('publish.html')


@app.route("/textlabel.html")
def textlabel():
    return render_template('textlabel.html')


@app.route("/textlabel2.html")
def textlabel2():
    return render_template('textlabel2.html')


@app.route('/login/username/<user_name>/password/<pass_word>')
def username_login(user_name, pass_word):
    password = c.get_user_passwd(username=user_name)
    if password is not None:
        if password == pass_word:
            result = {'code': 0}
        elif password != pass_word:
            result = {'code': 1, 'message': 'Wrong password!'}
    else:
        result = {'code': 1, 'message': 'User doesn\'t exists!'}
    return jsonify(result)

@app.route('/login/email/<useremail>/password/<pass_word>')
def email_login(useremail, pass_word):
    password = c.get_user_passwd(useremail=useremail)
    if password is not None:
        if password == pass_word:
            result = {'code': 0}
        elif password != pass_word:
            result = {'code': 1, 'message': 'Wrong password!'}
    else:
        result = {'code': 1, 'message': 'User doesn\'t exists!'}
    return jsonify(result)


