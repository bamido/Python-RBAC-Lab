from flask import Flask
from app.routes import create_routes

app = Flask(__name__)

create_routes(app)

