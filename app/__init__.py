from flask import Flask, render_template
from app.config import Config
from app.routes import create_routes
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#import app.models.modelsref
from .models import modelsref
from app.models.mydb import db
from flask_login import LoginManager


def create_app():
    app = Flask(__name__)  # flask app object
    app.config.from_object(Config)  # application's configuration    
    db.init_app(app) # Initializing the database
    
    return app

app = create_app()  # Creating the app
create_routes(app) # Registering the blueprint
migrate = Migrate(app, db)  # Initializing the migration
login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    #print(user_id)
    #return ''' debug '''
    # Load and return a user instance based on user_id
    return models.modelsref.UserModel(user_id)

@login_manager.unauthorized_handler
def unauthorized():
    # Customize the unauthorized page here
    return render_template('auth/unauthorized.html'), 403  # You can customize the status code as well
