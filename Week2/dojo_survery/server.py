'''Coding Dojo - Flask Fundamentals - Dojo Survey

Created: 09/09/2017
Author: Frank J Genova

'''

from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
    '''Route for / to render index.html'''

    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    '''Route for /result to render result.html'''
    print("made it")
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comments = request.form['comments']
    render_template('result.html')
    return redirect('result.html')

app.run(debug=True)
