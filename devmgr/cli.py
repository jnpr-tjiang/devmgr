import click
from flask.cli import FlaskGroup

from devmgr.app import create_app


def create_devmgr(info):
    return create_app(cli=True)


@click.group(cls=FlaskGroup, create_app=create_devmgr)
def cli():
    """Main entry point"""


@cli.command("init")
def init():
    """Initialize devmgr app, create database tables and
    """
    from devmgr.extensions import db
    from devmgr import models
    click.echo("create devmgr database")
    db.create_all()
    click.echo("Done")


if __name__ == '__main__':
    cli()
