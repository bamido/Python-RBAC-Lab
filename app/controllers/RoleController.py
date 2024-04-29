from flask import Blueprint, render_template, request, redirect, url_for, flash, session, jsonify
from app.models.RoleModel import RoleModel, RoleForm
from app.config import Config
from app.models.mydb import db
from flask_login import login_required
from flask_wtf.csrf import generate_csrf

bp_role = Blueprint('bp_role', __name__)

@bp_role.route('/roles')
@login_required
def listroles():
    csrf_token = generate_csrf()
    #retrieve all roles
    roles = RoleModel.get_all_roles()
    return render_template('rbac/listroles.html', roles=roles, moduletitle="Access Control", title='Roles', app_name=Config.APP_NAME, author=Config.AUTHOR, csrf_token=csrf_token)

@bp_role.route('/addrole', methods=['GET', 'POST'])
@login_required
def addrole():
    base_url = request.host_url
    form = RoleForm(request.form)
    if request.method == 'POST':
        if form.validate():
            rolename = form.role_name.data

            newrole = RoleModel(role_name=rolename)
            db.session.add(newrole)
            db.session.commit()
            flash('Role added successfully.', 'success')  
            return jsonify({'success':True})
        else:
            errors = form.errors
            return jsonify({'errors':errors})

    return render_template('rbac/addrole.html', form=form, base_url=base_url)


@bp_role.route('/editrole/<int:id>', methods=['GET','POST'])
@login_required
def editrole(id):
    role = RoleModel.query.get_or_404(id)
    base_url = request.host_url
    form = RoleForm(request.form)
    if request.method == 'POST':
        if form.validate():
            role.role_name = form.role_name.data
            # Commit changes to the database
            db.session.commit()
            flash('Role updated successfully.', 'success')            
            return jsonify({'success':True})
        else:
            errors = form.errors
            return jsonify({'errors':errors})
    return render_template('rbac/editrole.html', form=form, role=role, base_url=base_url)


@bp_role.route('/deleterole/<int:id>', methods=['GET','DELETE'])
def deleterole(id):
    # Find the role record by ID
    role = RoleModel.query.get(id)
    if role:
        # Delete the role record from the database session
        db.session.delete(role)
        # Commit the session to permanently delete the record from the database
        db.session.commit()
        return jsonify({'message': 'Role deleted successfully'}), 200
    else:
        return jsonify({'message': 'Role not found'}), 404
