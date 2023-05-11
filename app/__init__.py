from flask import Flask
# import SQLAlchemy from flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy
# import Migrate from flask_migrate
from flask_migrate import Migrate
# import libraries
from dotenv import load_dotenv
# used to read environment variables
import os

# give us access to database operations
# instantiate the db
db = SQLAlchemy()
# instantiate the migrate
migrate = Migrate()
load_dotenv()

def create_app(test_config=None):
    app = Flask(__name__)

    # set up the database
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_DATABASE_URI")
    # connect the db and migrate to our Flask app
    db.init_app(app)
    migrate.init_app(app, db)

    # register the planet blueprints
    from .routes import planets_bp
    app.register_blueprint(planets_bp)

    return app