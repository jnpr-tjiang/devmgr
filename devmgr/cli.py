import click
from flask.cli import FlaskGroup

from devmgr.app import create_app


def create_devmgr(info):
    return create_app(cli=True)


@click.group(cls=FlaskGroup, create_app=create_devmgr)
def cli():
    """Main entry point"""


@cli.command()
def init():
    """Initialize devmgr app, create database tables and
    """
    from devmgr.extensions import db

    click.echo("Creating devmgr database tables ...")
    db.create_all()
    from sqlalchemy.schema import CreateTable
    from devmgr.models import Device, device_labels, Annotation, Label
    click.echo(CreateTable(Device.__table__).compile())
    click.echo(CreateTable(Annotation.__table__).compile())
    click.echo(CreateTable(Label.__table__).compile())
    click.echo(CreateTable(device_labels).compile())
    click.echo("Done")

if __name__ == '__main__':
    cli()
