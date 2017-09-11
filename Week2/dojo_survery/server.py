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

@app.route('/result', methods=['GET','POST'])
def form_content():
    '''Route for /result to render result.html'''

    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comments = request.form['comments']
    # render_template('result.html')
    context = {'name':name, 'location':location, 'language':language, 'comments':comments}
    # return render_template('result.html', **context)
    # name = "Frank J Genova"
    return render_template('result.html', **context)

app.run(debug=True)
