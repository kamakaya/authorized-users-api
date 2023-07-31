from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class AuthorizedUsers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50))
    user_email = db.Column(db.String(50))
    project_name = db.Column(db.String(50))
    manager_name = db.Column(db.String(50))

    def __init__(self, project_name, manager_name, user_name, user_email):
        self.user_name = user_name
        self.user_email = user_email
        self.project_name = project_name
        self.manager_name = manager_name