from flask import Flask, render_template, redirect, request, flash
import re

    
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'secret'
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'mydb')
# an example of running a query
# print (mysql.query_db("SELECT * FROM emails"))

@app.route('/')
def index():
    print("this is it")
    query = mysql.query_db("SELECT * FROM emails")
    print('{}'.format(query))
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    print('in check')
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
    if EMAIL_REGEX.match(request.form['email']) is None:
        flash('not an email')
        return redirect('/')
    else:
        print(request.form['email'])
        flash('the email you entered {} is valid'.format(request.form['email']))
        query = "SELECT * FROM emails WHERE email = :email"
        data = {
                'email': request.form['email']
    }
        check_unique = mysql.query_db(query, data)
        if len(check_unique) > 0:
            print('not unique email')
            flash('not unique email')
            redirect ('/')
        else:    
            query = "INSERT INTO emails (email, created_at, updated_at) \
                    VALUES (:email, now(), now()) "    
            data = {
                    'email': request.form['email']
            }
            mysql.query_db(query, data)
        return redirect('/success')

@app.route('/remove', methods=['POST'])
def delete():
    query = "SELECT * FROM emails where email = :email"
    data = {
        'email': request.form['email']
    }
    is_it_in_db = mysql.query_db(query, data)
    if len(is_it_in_db)==0:
        print('email not found')
        flash('email not found')
        return redirect('/success')
    else:
        query = "DELETE FROM emails WHERE email = :email"
        data = {'email': request.form['email']}         
        friends = mysql.query_db(query, data)
        return redirect('/success')    

@app.route('/success')
def show():
    print('success route')
    query = mysql.query_db("SELECT * FROM emails")
    email_list = query
    return render_template('success.html', email_list = email_list)
    
app.run(debug=True)