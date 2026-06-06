from .. import db
from datetime import datetime

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    filename = db.Column(db.String(120), nullable=False)
    upload_date = db.Column(db.DateTime, nullable=True)
    update_date = db.Column(db.DateTime, nullable=True)
    delete_date = db.Column(db.DateTime, nullable=True)
    ftp_status = db.Column(db.String(50), default='pending')
    server_id = db.Column(db.Integer, db.ForeignKey('server.id'), nullable=True)

    def __repr__(self):
        return f"<Project {self.name}>"
