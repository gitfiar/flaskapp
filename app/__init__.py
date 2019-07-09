from flask import Flask
from flask_appconfig import AppConfig
from flask_bootstrap import Bootstrap
import os
from .views import views
from config import Config 
from flask_sqlalchemy import SQLAlchemy


def create_app(configfile=None):
    # We are using the "Application Factory"-pattern here, which is described
    # in detail inside the Flask docs:
    # http://flask.pocoo.org/docs/patterns/appfactories/
    app = Flask(__name__)
    # We use Flask-Appconfig here, but this is not a requirement
    AppConfig(app)

    # Install our Bootstrap extension
    Bootstrap(app)

    # Our application uses blueprints as well; these go well with the
    # application factory. We already imported the blueprint, now we just need
    # to register it:
    app.register_blueprint(views)
    app.config.from_object(Config)
    Config.init_app(app)
    # Because we're security-conscious developers, we also hard-code disabling
    # the CDN support (this might become a default in later versions):
    # We initialize the navigation as well
    app.config.setdefault('BOOTSTRAP_SERVE_LOCAL', True)
    db = SQLAlchemy(app)
    db.init_app(app)
    
    app.jinja_env.trim_blocks = True
    app.jinja_env.lstrip_blocks = True

    return app




