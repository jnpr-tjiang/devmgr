from flask import Flask

from devmgr import api
from devmgr.extensions import db


def create_app(testing=False, cli=False):
    """Application factory, used to create application
    """
    app = Flask('devmgr')
    app.config.from_object('devmgr.config')

    if testing is True:
        app.config['TESTING'] = True

    configure_extensions(app, cli)
    register_blueprints(app)

    return app


def configure_extensions(app, cli):
    """Configure Flask extensions
    """
    db.init_app(app)


def register_blueprints(app):
    """Register blueprints
    """
    app.register_blueprint(api.views.blueprint)
