'''Coding Dojo - Flask Fundamentals - Assignment: Great Number Game

Created: 09/15/2017
Author: Frank J Genova

Create a site that when a user loads it creates a random number
between 1-100 and stores the number in session.
Allow the user to guess at the number and tell them when they are too high or too low.
If they guess the correct number tell them and offer to play again.
'''

import random
from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)

app.secret_key = "SecretKey"

@app.route('/')
def index():
    '''route to render index.html'''
    try:
        session['rand_int']
    except KeyError:
        rand_int = random.randint(1, 100)
        session['rand_int'] = rand_int
    if session['rand_int'] == 0:
        rand_int = random.randint(1, 100)
        session['rand_int'] = rand_int
    return render_template('index.html', visibility='invisible')

@app.route('/process', methods=["POST"])
def check_guess():
    '''route to check guess vs random int'''
    print('hello from 31')
    print("request.form['guess']", request.form['guess'] )
    session['guess'] = request.form['guess']
    rand_int = int(session['rand_int'])
    guess = int(session['guess'])
    print('rand_int:', rand_int)
    print('guess:', guess)
    if guess == rand_int:
        msg = 'you guessed right'
        visibility = 'visible'
        bg = 'bg-success'
    elif guess > rand_int:
        msg = 'your guess is too high'
        visibility = 'invisible'
        bg = 'bg-danger'
    else:
        msg = 'your guess is too low'
        visibility = 'invisible'
        bg = 'bg-danger'
    print(msg)
    context = {'msg':msg, 'visibility':visibility, 'bg':bg}
    return render_template('index.html', **context)

@app.route('/restart', methods=['POST'])
def restart():
    '''route to restart'''
    session['rand_int']=0
    rand_int=0
    print(session['rand_int'])
    print(rand_int)
    return redirect('/')


app.run(debug=True)

