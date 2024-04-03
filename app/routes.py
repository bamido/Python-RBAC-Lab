from flask import render_template
from app import app
import os
APP_NAME = os.getenv('APP_NAME')
author = os.getenv('AUTHOR')

@app.route('/')
@app.route('/login')
def login():
    return render_template('auth/signin.html', title='Sign In', app_name=APP_NAME, author=author)

@app.route('/register')
def register():
    return render_template('auth/signup.html', title='Sign Up', app_name=APP_NAME, author=author)

@app.route('/dashboard')
def dashboard():
    return render_template('portal/dashboard.html', title="Dashboard", app_name=APP_NAME, author=author)

