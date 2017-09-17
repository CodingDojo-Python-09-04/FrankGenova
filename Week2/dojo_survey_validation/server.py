'''Coding Dojo - Flask Fundamentals - Dojo Survey

Created: 09/09/2017
Author: Frank J Genova

'''

from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)

app.secret_key = '\x9f\x15-\x033"\x11\xb6\xfbw\xc8\xab\xaaJF]\xa2\xd4\xb6\xf6E\xcff\xfe'
@app.route('/')
def index():
    '''Route for / to render index.html'''       
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def form_content():
    '''Route for /result to render result.html'''
    ready = True
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comments = request.form['comments']

    if len(name) < 1:
        flash('Name is required')
        ready = False
    if len(comments) < 1:
        flash('Comments are required')
        ready = False
    if len(comments) > 120:
        flash('Comments exceed 120 characters')
        ready = False
    if not ready:
        return redirect(url_for('index'))
    
    context = {'name':name, 'location':location, 'language':language, 'comments':comments}
    return render_template('result.html', **context)

app.run(debug=True)

# FRANKs-MBP:Week2 frankgenova$ python
# Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 12:39:47)
# [GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import os
# >>> os.urandom(24)
# '\x9f\x15-\x033"\x11\xb6\xfbw\xc8\xab\xaaJF]\xa2\xd4\xb6\xf6E\xcff\xfe'
# >>>