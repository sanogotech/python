from flask import Flask
app = Flask(__name__)

import mysql.connector
from mysql.connector import Error

from  flask import jsonify
from  flask  import request
from werkzeug.security import  generate_password_hash, check_password_hash


@app.route("/")
def hello_www():
    return "Hello World Wide Web!"

@app.route('/user')
def user():
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='mysql',
                                       user='root',
                                       password='')

        cursor = conn.cursor()
        cursor.execute("SELECT * from user;")
        rows = cursor.fetchall()
        resp=jsonify(rows)
        resp.status_code=200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.errorhandler(404)
def not_found(error=None):
    message= {
        'status':404,
        'message':'Not Found :' +request.url,
        }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

if __name__ =="__main__":
    app.run()
