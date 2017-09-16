'''Coding Dojo - Flask Fundamentals - Assignment: Great Number Game

Created: 09/16/2017
Author: Frank J Genova

Create a game where user gets different amounts of gold,
when they click on Find Gold!
'''

import random
from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)

app.secret_key = "SecretKey"

@app.route('/')
def index():
    '''route to render index.html'''
    try:
        session['gold_stash']
    except KeyError:
        session['gold_stash'] = 0
    try:
        session['activities']
    except KeyError:
        session['activities'] = []
    gold_stash = session['gold_stash']
    activities = session['activities']
    context = {'gold_stash':gold_stash, 'activities':activities}
    return render_template('index.html', **context)

@app.route('/process_money', methods=["POST"])
def get_gold():
    '''route to get gold'''
    building = request.form['building']
    if building == 'farm':
        min_gold = 10
        max_gold = 20
        rand_gold = random.randint(min_gold, max_gold)
        session['gold_stash'] += rand_gold
        gold_stash = session['gold_stash']
        activity = 'Earned '+str(rand_gold)+' golds from the '+ building + '\n'
        session['activities'].append(activity)
        activities = session['activities']
    elif building == 'cave':
        min_gold = 5
        max_gold = 10
        rand_gold = random.randint(min_gold, max_gold)
        session['gold_stash'] += rand_gold
        gold_stash = session['gold_stash']
        activity = 'Earned '+str(rand_gold)+' golds from the '+ building + '\n'
        session['activities'].append(activity)
        activities = session['activities']
    elif building == 'house':
        min_gold = 2
        max_gold = 5
        rand_gold = random.randint(min_gold, max_gold)
        session['gold_stash'] += rand_gold
        gold_stash = session['gold_stash']
        activity = 'Earned '+str(rand_gold)+' golds from the '+ building + '\n'
        session['activities'].append(activity)
        activities = session['activities']
    elif building == 'casino':
        min_gold = -50
        max_gold = 50
        rand_gold = random.randint(min_gold, max_gold)
        session['gold_stash'] += rand_gold
        gold_stash = session['gold_stash']
        if rand_gold < 0:
            rand_gold = abs(int(rand_gold))
            activity = 'Lost '+str(rand_gold) + ' golds from the '+ building
            session['activities'].append(activity)
            activities = session['activities']
        else:
            activity = 'Earned '+str(rand_gold)+' golds from the '+ building + '\n'
            session['activities'].append(activity)
            activities = session['activities']
    else:
        print 'no building found'

    return redirect('/')

app.run(debug=True)
