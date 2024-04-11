from flask import Flask
from app.config import Config
from app.routes import create_routes
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import app.models.modelsref
from app.models.mydb import db


def create_app():
    app = Flask(__name__)  # flask app object
    app.config.from_object(Config)  # application's configuration    
    db.init_app(app) # Initializing the database
    
    return app

app = create_app()  # Creating the app
create_routes(app) # Registering the blueprint
migrate = Migrate(app, db)  # Initializing the migration