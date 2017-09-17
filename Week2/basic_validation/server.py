'''Coding Dojo - Flask Fundamentals - Assignment: Basic Form Validation

Created: 09/16/2017
Author: Frank J Genova

Lean basic form validation using examples from Coding Dojo website.
'''

from flask import Flask, render_template, redirect, request, session, flash

app = Flask(__name__)

app.secret_key = '\xfe\xe5\x97\xfc\xdf%Y8\xe9\x14\xf2{\x0fC\x97\n\x07&\x03\x10\xeb\xb9\xa5\xb0'

@app.route('/')
def index():
    '''route for index'''

    return render_template('index.html')
@app.route('/process', methods=['Post'])

def process():
    '''route for validation'''
    # import pdb; pdb.set_trace()
    if len(request.form['name']) < 1:
        flash("Name cannot be empty")
    else:
        flash("Success! Your name is {}".format(request.form['name']))
    return redirect('/')

app.run(debug=True)
