from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()  # Define db once

def init_db(app):
    db.init_app(app)
    Migrate(app, db)