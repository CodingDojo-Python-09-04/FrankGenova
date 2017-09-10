'''Coding Dojo - Flask Fundamentals - Assignment: Landing Page

Created: 09/10/2017
Author: Frank J Genova
see about.md for details
'''

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    '''Render view for /'''

    return render_template('index.html')

@app.route('/ninjas')
def ninjas():
    '''Render view for /ninjas'''

    return render_template('ninjas.html')

@app.route('/dojos/new')
def dojos_new():
    '''Render view for /dojos/new'''

    return render_template('dojos.html')

def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()

