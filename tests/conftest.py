import pytest

from devmgr.models import Device
from devmgr.app import create_app
from devmgr.extensions import db as _db


@pytest.fixture
def app():
    app = create_app(testing=True)
    return app


@pytest.fixture
def db(app):
    _db.app = app

    with app.app_context():
        _db.create_all()

    yield _db

    _db.session.close()
    _db.drop_all()


@pytest.fixture
def device(db):
    device = Device(
        name='my-qfx-1',
        serial='DF588'
    )

    db.session.add(device)
    db.session.commit()

    return device
