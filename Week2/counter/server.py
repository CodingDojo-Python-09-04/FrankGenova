'''Coding Dojo - Flask Fundamentals - Dojo Survey

Created: 09/09/2017
Author: Frank J Genova

'''

from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = "secretkey"


@app.route('/', methods=['GET','POST'])
def index():
    '''Route for / to render index.html and record count'''
    print("i did render 1")
    try:
        session['count']
    except KeyError:
        session['count'] = 0
    temp_int = int(session['count'])
    temp_int += 1
    session['count'] = temp_int
    if session['count'] == 1:
        msg=str(session['count']) + ' time'
    else:
        msg=str(session['count']) + ' times'
    return render_template('index.html', times=msg)

@app.route('/add2', methods=['POST'])
def add2():
    '''Route for /result to add 2 and render index.html'''

    print('in route /')
    temp_int = int(session['count'])
    temp_int += 2
    session['count'] = temp_int
    msg=str(session['count']) + ' times'
    return render_template('index.html',times=msg)

@app.route('/reset', methods=['POST'])
def reset():
    '''Route for /reset to  and render index.html'''

    print('in /reset')
    temp_int = int(session['count'])
    temp_int = 0
    session['count'] = temp_int
    msg=str(session['count']) + ' times'
    return render_template('index.html',times=msg)

app.run(debug=True)
