from devmgr.extensions import db


class Annotation(db.Model):
    """Key-value annotations for any config object. Annotated value is usually
    a json blob that is not indexed
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    value = db.Column(db.JSON)
    device_id = db.Column(
        db.Integer, db.ForeignKey('device.id'), nullable=False
    )
    __table_args__ = (
        db.UniqueConstraint('name', 'device_id', name='unique_key_value'),
    )

    def __repr__(self):
        return '<Annotation %s>' % self.name
