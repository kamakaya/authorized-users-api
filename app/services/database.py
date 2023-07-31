import os
from app.models.authorized_users import db

def setup_database(app):
    env = os.environ.get('ENV', 'production')

    if env == 'development':
        database_uri = 'mysql+pymysql://root@localhost/deloitte_gcp_test'
    else:
        db_user = os.environ["DB_USER"]
        db_pass = os.environ["DB_PASS"]
        db_name = os.environ["DB_NAME"]
        cloud_sql_connection_name = os.environ["CLOUD_SQL_CONNECTION_NAME"]

        database_uri = (
            f"mysql+pymysql://{db_user}:{db_pass}@/{db_name}"
            f"?unix_socket=/cloudsql/{cloud_sql_connection_name}"
        )

    app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
