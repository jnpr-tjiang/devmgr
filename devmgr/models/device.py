from devmgr.extensions import db

device_labels = db.Table(
    'device_labels',
    db.Column('label_id', db.Integer, db.ForeignKey('label.id'), primary_key=True),
    db.Column('device_id', db.Integer, db.ForeignKey('device.id'), primary_key=True)
)

device_annotations = db.Table(
    'device_annotations',
    db.Column('annotation_id', db.Integer, db.ForeignKey('annotation.id'), primary_key=True),
    db.Column('device_id', db.Integer, db.ForeignKey('device.id'), primary_key=True)
)


class Device(db.Model):
    """Device data model
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    serial = db.Column(db.String(40), unique=True)
    labels = db.relationship(
        'Label', secondary=device_labels, lazy='subquery', backref=db.backref('devices', lazy=True)
    )
    annotations = db.relationship(
        'Annotation', secondary=device_annotations, lazy='subquery', backref=db.backref('devices', laze=True)
    )

    def __repr__(self):
        return "<Device %s (sn=%s)>" % (self.name, self.serial)
