from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.UserModel import UserModel, SignupForm
from app.config import Config
from app.models.mydb import db
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash


bp_authcontroller = Blueprint('bp_authcontroller', __name__)

@bp_authcontroller.route('/')
@bp_authcontroller.route('/login')
def login():
    return render_template('auth/signin.html', title='Sign In', app_name=Config.APP_NAME, author=Config.AUTHOR)
@bp_authcontroller.route('/register', methods=['GET', 'POST'])
def register():
    form = SignupForm(request.form)
    #print(request.form)
    if request.method == 'POST' and form.validate():
        # Extract data from the form
        username = form.username.data
        email = form.email_address.data
        password = form.password.data
        lastname = form.lastname.data
        firstname = form.firstname.data

        # Check if the email already exists in the database
        existing_user = UserModel.query.filter_by(email_address=email).first()
        if existing_user:
            # Handle duplicate email address (e.g., display an error message)
            flash('Email address already exists.', 'error')            
            return render_template('auth/signup.html', title='Sign Up', app_name=Config.APP_NAME, author=Config.AUTHOR, form=form)


        # If the email address doesn't exist, proceed with inserting the new record
        try:
            # Create a new user object
            hashed_password = generate_password_hash(password)
            new_user = UserModel(
                username=username,
                email_address=email,
                password=hashed_password,
                lastname=lastname,
                firstname=firstname,
                role_id=3
            )

            db.session.add(new_user)
            db.session.commit()
            msg = "Dear {} {}, your account creation was successfull! Use the form below to login"
            flash(msg.format(firstname, lastname), 'success')
            return render_template('auth/signin.html', title='Sign In', app_name=Config.APP_NAME, author=Config.AUTHOR, msg=msg)
        except IntegrityError as e:
            # Handle IntegrityError (e.g., rollback the transaction, display an error message)
            db.session.rollback()
            error_info = e.orig.args  # Get the original error message
            flash(f'Error: {error_info}', 'error')
            return render_template('auth/signup.html', title='Sign Up', app_name=Config.APP_NAME, author=Config.AUTHOR, form=form)

    return render_template('auth/signup.html', title='Sign Up', app_name=Config.APP_NAME, author=Config.AUTHOR, form=form)
