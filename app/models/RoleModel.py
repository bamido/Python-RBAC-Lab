from app.models.mydb import db

class RoleModel(db.Model):
    __tablename__ = 'roles'

    role_id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(50), unique=True, nullable=False)
    created_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.current_timestamp())
    updated_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    users = db.relationship('UserModel', backref='role', lazy=True)
    privileges = db.relationship('PrivilegeModel', backref='role', lazy=True)

    def __repr__(self):
        return '<RoleModel {}>'.format(self.role_name)

    @staticmethod
    def get_all_roles():
        # Sample method to retrieve all users
        return {1:"Super Admin", 2:"Software Engineer", 3:"Member"}  # Example data
