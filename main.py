from flask import Flask, render_template, redirect, request, flash
from data import db_session
from data.users import User
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config['SECRET_KEY'] = 'andrew-bakradze'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('index3.html')


@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == 'POST':
        pass
    return render_template('index4.html')



def main():
    db_session.global_init("db/subScript.db")
    app.run(port=8000, host='127.0.0.1')

if __name__ == '__main__':
    main()