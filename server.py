from flask import flash
from flask import Flask
from flask import request
from flask import render_template

from model import Account
from model import connect_to_db
from model import db


app = Flask(__name__)
app.secret_key = "ABC"


@app.route('/', methods=['GET'])
def homepage():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def create_account():
    db.session.add(
	Account(
	    first_name=request.form['first_name'],
	    last_name=request.form['last_name'],
	    email=request.form['email'],
            password=request.form['password'],
            picture='some picture url ?',
	),
    )
    db.session.commit()
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    account = Account.query.filter_by(email=request.form['email']).first()
    if account or account.password != request.form['password']:
        flash('Invalid email/password combo!')
    return render_template('index.html')

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0')
