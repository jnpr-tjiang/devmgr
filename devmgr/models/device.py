from devmgr.extensions import db


class Device(db.Model):
    """Device data model
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    serial = db.Column(db.String(40), unique=True)

    def __repr__(self):
        return "<Device %s" % self.name
