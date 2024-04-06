from flask import Blueprint, render_template
from app.models.RoleModel import RoleModel
from app.config import Config

bp_rolecontroller = Blueprint('bp_rolecontroller', __name__)

@bp_rolecontroller.route('/roles')
def listroles():
    # Assuming RoleModel has a method to retrieve all roles
    roles = RoleModel.get_all_roles()
    return render_template('rbac/listroles.html', roles=roles, )