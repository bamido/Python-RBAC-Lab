from app.models.mydb import db
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email


class UserModel(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.role_id'), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email_address = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    firstname = db.Column(db.String(50), nullable=False)
    phonenumber = db.Column(db.String(20))
    dateofbirth = db.Column(db.Date)
    created_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.current_timestamp())
    updated_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def __repr__(self):
        return '<UserModel {}>'.format(self.username)
   
    @staticmethod
    def get_all_users():
        # Sample method to retrieve all users
        return ["Elon Musk", "Tim Cook", "Larry Page", 'Yemi Bamido', 'Toluwani Bamido']  # Example data


class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message="Please, enter your username!")])
    email_address = StringField('Email', validators=[DataRequired(message="Please enter your email address."), Email(message="Please enter a valid Email adddress!")])
    password = PasswordField('Password', validators=[DataRequired(message="Please, enter your password!")])
    lastname = StringField('Last Name', validators=[DataRequired(message="Please, enter your lastname!")])
    firstname = StringField('First Name', validators=[DataRequired(message="Please, enter your firstname!")])
    phonenumber = StringField('Phone Number')
    dateofbirth = StringField('Date of Birth')
    terms = BooleanField('Terms', validators=[DataRequired(message="You must agree before submitting.!")])
    submit = SubmitField('Sign Up')
