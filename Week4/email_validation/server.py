from flask import Flask, render_template, redirect, request
import re

    
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'mydb')
# an example of running a query
print (mysql.query_db("SELECT * FROM users"))

@app.route('/')
def index():
    print("this is it")
    # query = mysql.query_db("SELECT * FROM users")
    # print('{}'.format(query))
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    print('in check')
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
    if EMAIL_REGEX.match(request.form['email']) is None:
        print('not an email')
    else:
        print(request.form['email'])

    return redirect ('/')

app.run(debug=True)