'''Coding Dojo - Flask Fundamentals - Assignment: Basic Form Validation

Created: 09/16/2017
Author: Frank J Genova

Lean basic form validation using examples from Coding Dojo website.
'''

from flask import Flask, render_template, redirect, request, session, flash

app = Flask(__name__)

app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/')
def index():
    '''route for index'''

    return render_template('index.html')
@app.route('/process', methods=['Post'])

def process():
    '''route for validation'''

    if len(request.form['name']) < 1:
        flash("Name cannot be empty")
    else:
        flash("Success! Your name is {}".format(request.form['name']))
    return redirect('/')

app.run(debug=True)
