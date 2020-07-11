import dateutil.parser
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from flask_login import LoginManager

conf = Config()

sqlalchemy = SQLAlchemy()
login = LoginManager()

def create_app(configuration):
    application = Flask(__name__)
    # Set App Configuration
    application.config.from_object(configuration)

    sqlalchemy.init_app(application)

    login.init_app(application)
    login.login_view = 'bp.login'
    register_blueprints(application)

    return application

def register_blueprints(app):
    from app.routes import bp
    app.register_blueprint(bp)
