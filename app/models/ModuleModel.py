from app.models.mydb import db

class ModuleModel(db.Model):
    __tablename__ = 'modules'

    module_id = db.Column(db.Integer, primary_key=True)
    module_title = db.Column(db.String(100), unique=True, nullable=False)
    module_order = db.Column(db.Integer, nullable=False)
    module_icon = db.Column(db.String(50))
    created_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.current_timestamp())
    updated_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    tasks = db.relationship('TaskModel', backref='module', lazy=True)

    def __repr__(self):
        return '<ModuleModel {}>'.format(self.module_title)