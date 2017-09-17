'''Coding Dojo - Flask Fundamentals - Assignment: Dissappearing Ninjas

Created: 09/17/2017
Author: Frank J Genova

Show Ninjas vasedon user input
'''

from flask import Flask, render_template, redirect, request, session, flash

app = Flask(__name__)

app.secret_key = '\xfe\xe5\x97\xfc\xdf%Y8\xe9\x14\xf2{\x0fC\x97\n\x07&\x03\x10\xeb\xb9\xa5\xb0'

@app.route('/')
def index():
    '''route for index'''
    return render_template('index.html')

@app.route('/ninja')
def ninja():
    '''route for general ninja'''
    # import pdb; pdb.set_trace()
    color = 'all'
    print(color)
    return render_template('ninja.html', color=color)

@app.route('/ninja/<color>')
def color_ninja(color):
    ''' make specific color '''
    print(color)
    ok_colors = ['red','orange','purple','blue']
    if color not in ok_colors:
        print('color not found')
        color="not_found"
    return render_template("ninja.html", color=color)

app.run(debug=True)
