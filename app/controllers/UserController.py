from flask import Blueprint, render_template
from app.models.UserModel import UserModel
from app.config import Config


bp_usercontroller = Blueprint('bp_usercontroller', __name__)

@bp_usercontroller.route('/users')
def listusers():
    # get all users
    users = UserModel.get_all_users()
    return render_template('rbac/listusers.html', users=users, title="Users")
