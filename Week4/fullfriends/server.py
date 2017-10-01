from flask import Flask, render_template, redirect, request, flash
import re

    
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'secret'
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'fullfriendsdb')
# an example of running a query
# print (mysql.query_db("SELECT * FROM emails"))

@app.route('/')
def index():
    friends = mysql.query_db("SELECT * FROM friends")
    return render_template('index.html', friends = friends)

@app.route('/friends', methods=['POST'])
def create():
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
    if EMAIL_REGEX.match(request.form['email']) is None:
        print('not an email')
        return redirect('/')
    else:
        print(request.form['email'])
        print('the email you entered {} is valid'.format(request.form['email']))
        query = "SELECT * FROM friends WHERE email = :email"
        data = {
                'email': request.form['email']
    }
        check_unique = mysql.query_db(query, data)
        if len(check_unique) > 0:
            print('not unique email')
            flash('not unique email')
            redirect ('/')
        else:
            print('we made 51 else')    
            query = "INSERT INTO friends (first_name, last_name, email, created_at, updated_at) \
                    VALUES (:first_name, :last_name, :email, now(), now()) "    
            data = {
                    'first_name': request.form['first_name'],
                    'last_name': request.form['last_name'],
                    'email': request.form['email']
            }
            print('we made it to 59')
            update = mysql.query_db(query, data)
            friends = mysql.query_db("SELECT * FROM friends")
            return render_template('index.html', friends = friends)

@app.route('/friends/<id>/edit')
def edit(id):
    print('in edit')
    query = "SELECT * FROM friends WHERE id=:id"
    data = {
            'id': id
    }
    friends = mysql.query_db(query, data)[0]
    return render_template('friends.html', friends = friends)

@app.route('/friends/<id>', methods=['POST'])
def update(id):
    print('in update')
    query = "UPDATE  friends \
            SET  first_name = :first_name, last_name = :last_name, email = :email \
            WHERE id = :id"
            
    data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'id': id
    }         
    update = mysql.query_db(query, data)
    print("we did 74")
    friends = mysql.query_db("SELECT * FROM friends")
    return render_template('index.html', friends = friends)   
    
@app.route('/friends/<id>/delete', methods=['POST'])
def destroy(id):
    print('in destroy')
    query = "DELETE FROM friends  WHERE id = :id"
    data = {'id': id}         
    friends = mysql.query_db(query, data)
    return redirect('/')
        
app.run(debug=True)