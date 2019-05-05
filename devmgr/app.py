from flask import Flask

from devmgr.extensions import db


def create_app(testing=False, cli=False):
    """Application factory, used to create application
    """
    app = Flask('devmgr')
    app.config.from_object('devmgr.config')

    if testing is True:
        app.config['TESTING'] = True

    configure_extensions(app, cli)

    return app


def configure_extensions(app, cli):
    """Configure Flask extensions
    """
    db.init_app(app)
