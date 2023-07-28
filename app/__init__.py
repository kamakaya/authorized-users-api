from flask import Flask
# from .models.project import db
# from .services.database import setup_database
from .routes.authorized_users import authorized_users_blueprint

def create_app():
    app = Flask(__name__)
    # setup_database(app)
    # db.init_app(app)

    app.register_blueprint(authorized_users_blueprint)

    return app
