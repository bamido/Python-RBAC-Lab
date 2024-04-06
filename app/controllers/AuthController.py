from flask import Blueprint, render_template
from app.models.UserModel import UserModel
from app.config import Config

bp_authcontroller = Blueprint('bp_authcontroller', __name__)

@bp_authcontroller.route('/')
@bp_authcontroller.route('/login')
def login():
    return render_template('auth/signin.html', title='Sign In', app_name=Config.APP_NAME, author=Config.AUTHOR)

@bp_authcontroller.route('/register')
def register():
    return render_template('auth/signup.html', title='Sign Up', app_name=Config.APP_NAME, author=Config.AUTHOR)
