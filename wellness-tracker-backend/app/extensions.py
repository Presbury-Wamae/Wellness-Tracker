# app/extensions.py
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS

# Initialize extensions without binding to an app yet
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
cors = CORS()

