'''Coding Dojo - Flask Fundamentals - More Routing

Created: 09/09/2017
Author: Frank J Genova
see about.md
'''

from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/')
def index():
    '''Route for / return index.html'''

    return render_template('index.html')

@app.route('/users', methods=['POST'])
def create_user():
    print "Got Post Info"
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    return redirect('/show')

@app.route('/show')
def show_user():
    return render_template('user.html')

def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()
    
