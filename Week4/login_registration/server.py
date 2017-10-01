'''Coding Dojo - Flask + MySQL - Assignment: The Wall

Created at: 9/30/2017
Author: Frank J Genova

Create log in and registration.  Post messaages and allow comments.
Posts from newest to oldest.  Messages from oldest to newest. 
'''

from flask import Flask, request, render_template
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)
app.secret_key = 'secret'
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'walldb')

# this will load a page that has 2 forms one for registration and login
@app.route('/', methods=['GET'])
def index():
    #login and registration page
    email = session.form['email']
    password = session.form['password']
    flash(session, password)
    return render_template('index.html')
 
@app.route('/create_user', methods=['POST'])
def create_user():
 email = request.form['email']
 first_name = request.form['first_name']
 last_name = request.form['last_name']
 password = request.form['password']
 # run validations and if they are successful we can create the password hash with bcrypt
 pw_hash = bcrypt.generate_password_hash(password)
 # now we insert the new user into the database
 insert_query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:last_name, :first_name, :email, :password, NOW(), NOW())"
 query_data = { 'first_name': first_name, 'last_name': last_name, 'email': email, 'password': password }
 mysql.query_db(insert_query, query_data)
 # redirect to success page


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