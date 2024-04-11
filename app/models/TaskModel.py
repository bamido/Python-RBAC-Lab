from app.models.mydb import db

class TaskModel(db.Model):
    __tablename__ = 'tasks'

    task_id = db.Column(db.Integer, primary_key=True)
    module_id = db.Column(db.Integer, db.ForeignKey('modules.module_id'), nullable=False)
    task_label = db.Column(db.String(100), nullable=False)
    task_url = db.Column(db.String(100))
    task_route = db.Column(db.String(100))
    task_method = db.Column(db.String(10))
    task_icon = db.Column(db.String(50))
    isdashboard = db.Column(db.Boolean, default=False)
    isnavbar = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.current_timestamp())
    updated_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    privileges = db.relationship('PrivilegeModel', backref='task', lazy=True)


    def __repr__(self):
        return '<TaskModel {}>'.format(self.task_id)