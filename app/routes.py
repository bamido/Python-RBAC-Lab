from flask import Blueprint

main_blueprint = Blueprint('main', __name__)

# import from controllers
from app.controllers.AuthController import bp_authcontroller
from app.controllers.RoleController import bp_rolecontroller
from app.controllers.UserController import bp_usercontroller
from app.controllers.HomeController import bp_home


# Define your routes and map them to controllers
# Registering the blueprint
def create_routes(app):
    app.register_blueprint(bp_authcontroller)
    app.register_blueprint(bp_rolecontroller)
    app.register_blueprint(bp_usercontroller)
    app.register_blueprint(bp_home)

