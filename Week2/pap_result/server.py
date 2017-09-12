'''PAPpy Create Fake PAP Result

Created: 09/12/2017
Author: Frank J Genova

Given a text file with HL7 of incoming PAP results
supply a de-identified patient name and date of birth
and replace the message segments with the de-identified input
'''

from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
    '''Route for / to render index.html to show the main input form'''

    return render_template('index.html')

@app.route('/result', methods=['GET', 'POST'])
def form_content():
    '''Route for /result to render result.html'''

    name = request.form['name'] #user supplied fake name
    dob = request.form['dob'] #user supplied fake dob
    context = {'name':name, 'dob':dob}
    return render_template('result.html', **context)

app.run(debug=True)
