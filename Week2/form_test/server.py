'''Coding Dojo - Flask Fundamentals - More Routing

Created: 09/09/2017
Author: Frank J Genova
see about.md
'''

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    '''Route for / return index.html'''

    return render_template('index.html')

@app.route('/users', methods=['POST'])
def create_user():
    print "Got Post Info"
    name = request.form['name']
    email = request.form['email']
    return redirect('/')

def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()
    
