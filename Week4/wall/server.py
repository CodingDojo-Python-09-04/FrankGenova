'''Coding Dojo - Flask + MySQL - Assignment: The Wall

Created at: 9/30/2017
Author: Frank J Genova

Create log in and registration.  Post messaages and allow comments.
Posts from newest to oldest.  Messages from oldest to newest. 
'''

from flask import Flask, flash, request, render_template, session, redirect
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)
app.secret_key = 'secret'
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'walldb')

# load a page that has 2 forms one for registration and login
@app.route('/')
def index():
    # debug_msg('index')
    return render_template('index.html')

# validate login credentials
@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
    query_data = { 'email': email }
    user = mysql.query_db(user_query, query_data) # user will be returned in a list
    try:
        user[0]
    except IndexError:
        err_msg('Wrong *Email/Password')
        return render_template('index.html')
    if bcrypt.check_password_hash(user[0]['password'], password):
        # login user
        first_name = user[0]['first_name']
        user_id = user[0]['id']
        print(first_name, user_id, email)
        session['email'] = email
        session['user_id'] = user_id
        session['first_name'] = first_name
        messages = message_list()
        context = {
        'first_name': user[0]['first_name'],
        'messages': messages
    }
        return render_template('wall.html', **context)
        # return render_template('wall.html', first_name = first_name)
    else:
        # set flash error message and redirect to login page
        err_msg('Wrong Email/*Password')
        return render_template('index.html') 

# register user
@app.route('/register', methods=['POST'])
def register():
    email = request.form['email']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    # run validations and if they are successful we can create the password hash with bcrypt
    if password != confirm_password:
        err_msg('Password/Confirm Password Not the Same')
        return render_template('index.html')
    user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
    query_data = { 'email': email }
    user = mysql.query_db(user_query, query_data) # user will be returned in a list
    print(user)
    print(len(user))
    if len(user) == 1:
        err_msg('Email In Use')
        return render_template('index.html')
    pw_hash = bcrypt.generate_password_hash(password)
    # insert the new user into the database
    insert_query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"
    query_data = { 'first_name': first_name, 'last_name': last_name, 'email': email, 'password': pw_hash }
    mysql.query_db(insert_query, query_data)
    # debug_msg('register')
    return render_template('wall.html', first_name = first_name)

# post message
@app.route('/message', methods=['POST'])
def message():
    message = request.form['message']
    email = session['email']
    print('session email: {}'.format(email))
    query = 'SELECT *  FROM users WHERE email=:email'
    data = {
        'email': email
    }
    user = mysql.query_db(query, data)
    print('user {}'.format(user))
    user_id = user[0]['id']
    print('user_id: {}'.format(user_id))
    # insert the new message into the database
    insert_query = "INSERT INTO messages (user_id, message, created_at, updated_at) VALUES (:user_id, :message, NOW(), NOW())"
    query_data = { 'user_id': user_id, 'message': message }
    mysql.query_db(insert_query, query_data)
    # debug_msg('message', message + " from " + email)
    messages = message_list()
    context = {
        'first_name': user[0]['first_name'],
        'messages': messages
    }
    return render_template('wall.html', **context)

# show message comments
@app.route('/message_comments', methods=['POST'])
def message_comments():
    message_id = request.form['message_id']
    print('message id: {}'.format(message_id))
    query = single_message(message_id)
    return render_template('wall.html', single_message=query)

# post comment
@app.route('/comment', methods=['POST'])
def post_comment():
    print(request.form)
    message_id = request.form['single_message_id']
    comment = request.form['comment']
    user_id = session['user_id']
    print(user_id)
    # debug_msg('post_comment', message_id)
    print('message id: {}'.format(message_id))
    print('comment: {}'.format(comment))
    insert_query = "INSERT INTO comments (user_id, message_id, comments, created_at, updated_at) VALUES (:user_id, :message_id, :comment, NOW(), NOW())"
    query_data = { 'user_id': user_id, 'message_id': message_id, 'comment': comment }
    mysql.query_db(insert_query, query_data)
    # debug_msg('comment', comment)
    comments = comment_list(message_id)
    query = 'SELECT * FROM users WHERE users.id = :id'
    data = {
        'id': session['user_id']
    }
    first_name = mysql.query_db(query,data)[0]['first_name']
    print(first_name)
    context = {
        'first_name': first_name,
        'comments': comments,
        'single_message': single_message(message_id)
    }
    return render_template('wall.html', **context)

# show all posts
@app.route('/show')
def show():
    query = message_list()
    context = {
        'first_name': session['first_name'],
        'messages': query
    }
    return render_template('wall.html', **context)

# log out
@app.route('/log_out')
def log_out():
    session.clear()
    return redirect ('/')

# helper routines 
def char_repeat(char, rep):
    print(char*rep)

def message_list():
    query = 'SELECT users.last_name, users.first_name, messages.updated_at, \
    messages.message, messages.id FROM messages JOIN users ON messages.user_id = users.id \
    ORDER BY messages.updated_at DESC'
    messages = mysql.query_db(query)
    # debug_msg('messages', messages)
    return messages

def single_message(id):
    query = 'SELECT users.last_name, users.first_name, messages.updated_at, \
    messages.message, messages.id FROM messages JOIN users ON messages.user_id = users.id \
    WHERE messages.id = :id'
    data = {
        'id': id
    }
    message = mysql.query_db(query, data)[0]
    # debug_msg('single_message', message)
    return message

def comment_list(id):
    query = 'SELECT comments.id, comments.updated_at, comments.comments, users.first_name, users.last_name FROM comments JOIN users\
            ON comments.user_id = users.id \
            WHERE comments.message_id = :id'
    data = {
            'id':id
     }
    comments = mysql.query_db(query, data)
    # debug_msg('comments', comments)
    return comments
    
# error messages
def err_msg(msg):
    char_repeat('*', 40)
    flash('error: {}'.format(msg))
    print('error: {}'.format(msg))
    char_repeat('*', 40)
    return render_template('index.html')    

#debug routines
def debug_msg(route, query=None):
    char_repeat('*', 40)
    flash('route: {}'.format(route))
    print('route: {}'.format(route))
    if route == 'login':
        flash('email: {}'.format(request.form['email']))
        print('email: {}'.format(request.form['email']))
        flash('password: {}'.format(request.form['password']))
        print('password: {}'.format(request.form['password']))
        flash('query: {}'.format(query))
        print('query: {}'.format(query))
    elif route == 'register':
        flash('email: {}'.format(request.form['email']))
        print('email: {}'.format(request.form['email']))
        flash('password: {}'.format(request.form['password']))
        print('password: {}'.format(request.form['password']))
        flash('confirm_password: {}'.format(request.form['confirm_password']))
        print('confirm_password: {}'.format(request.form['confirm_password']))
        flash('query: {}'.format(query))
        print('query: {}'.format(query))
    elif route == 'message':
        flash('message from email: {}'.format(query))
        print('message from email: {}'.format(query))
    elif route == 'messages':
        flash('messages: {}'.format(query))
        print('messages: {}'.format(query))
    elif route == 'single_message':
        flash('single_message: {}'.format(query))
        print('single_message: {}'.format(query))
    elif route == 'post_comment':
        flash('post_comment: {}'.format(query))
        print('post_comment: {}'.format(query))


        pass    
    char_repeat('*', 40)    

################
# Legacy Below #
################

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