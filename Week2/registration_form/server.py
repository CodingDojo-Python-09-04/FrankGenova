'''Coding Dojo - Flask Fundamentals - Assignment: Registration Form

Created: 09/17/2017
Author: Frank J Genova

Create a simple registration page with the following fields:
email
first_name
last_name
password
confirm_password

Here are the validations you must include:
All fields are required and must not be blank
First and Last Name cannot contain any numbers
Password should be more than 8 characters
Email should be a valid email
Password and Password Confirmation should match

When the form is submitted, make sure the user submits appropriate information.
If the user did not submit appropriate information, return the error(s) above
the form that asks the user to correct the information.

Message Flashing with Categories
For this, you will need to use flash messages at the very least.
You may have to take this one step further and add categories to the flash messages.
You can learn that from the flask doc: flash messages with categories

If the form with all the information is submitted properly,
simply have it say a message "Thanks for submitting your information."

Ninja Version:
Add the validation that requires a password to have at least 1 uppercase letter
and 1 numeric value.

Hacker Version:
Add a birth-date field that must be validated as a valid date (and must be from the past).

'''
import datetime as dt
import re
from flask import Flask, render_template, request, redirect, session, flash, url_for

app = Flask(__name__)

app.secret_key = '\xd7\xb7\x04\xbbF\x8c\x81\x94\x0fu\x00$\xa3?\xe1\r\xb0\r\xe6\xa9\xf9\xd7\xd0\xdd'

@app.route('/')
def index():
    '''Route for / return index.html'''
    try:
        session['email']
    except KeyError:
        session['email'] = ''
    try:
        session['last_name']
    except KeyError:
        session['last_name'] = ''
    try:
        session['first_name']
    except KeyError:
        session['first_name'] = ''
    try:
        session['birthdate']
    except KeyError:
        session['birthdate'] =''            
    email = session['email']
    last_name = session['last_name']
    first_name = session['first_name']
    birthdate = session['birthdate']
    context = {'email':email, 'last_name':last_name, 'first_name':first_name, 'birthdate':birthdate}
    return render_template('index.html', **context)

@app.route('/process', methods=['POST'])
def validate():
    '''validate input'''

    NUMBER_REGEX = re.compile(r'\d+')
    UPPER_REGEX = re.compile(r'[A-Z]+')
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
    

    for key, value in request.form.items():
        if key == 'last_name' or key == 'first_name':
            if NUMBER_REGEX.search(value):
                flash('Numbers are not allowed in first or last name', 'alert-danger')
            continue
        if key == 'email' and not EMAIL_REGEX.match(value):
            flash('not a valid email', 'alert-danger')
            continue
        if (key == 'password' or key == 'confirm_password') and len(value) < 9:
            flash('Password and Confirmation must be greater than 8 characters', 'alert-danger')
        if (key == 'password' or key == 'confirm_password') and not UPPER_REGEX.match(value):
            flash('Password and Confirmation must contain an Upper case letter', 'alert-danger')  
        if (key == 'password' or key == 'confirm_password') and not NUMBER_REGEX.search(value):
            flash('Password and Confirmation must contain a number', 'alert-danger')     
    
    birthdate = request.form['birthdate']
    print('birthdate: {}'.format(session['birthdate']))
    # birthdate = dt.datetime.strptime(request.form.get('birthdate'))
    today = dt.datetime.today()
    print(type(today))
    print(today)
    redo_bd = dt.datetime.strptime(birthdate, '%Y-%m-%d')
    print('redo_bd {}'.format(redo_bd))
    print(type(redo_bd))
    print('now - bd {}'.format(today - redo_bd))
    if  redo_bd >= today:
        flash('Birthdate must be in the past','alert-danger') 

    if request.form.get('password') != request.form.get('confirm_password'):
        flash('Password and Confirmation do not match', 'alert-danger')

    session['email'] = request.form['email']
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['password'] = request.form['password']
    session['confirm_password'] = request.form['confirm_password']
    session['birthdate'] = request.form['birthdate']
    flash('Thanks for submitting your information','alert-success')
    return redirect(url_for('index'))

app.run(debug=True)
