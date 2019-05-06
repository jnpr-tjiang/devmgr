from devmgr.extensions import db


class Label(db.Model):
    """Key-value labels to search config objects. Both key and value are
    indexed and key-value pair must be unique.
    """
    __table_args__ = (
        db.UniqueConstraint('name', 'value', name='unique_key_value'),
    )
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    value = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return "<Label (%s: %s)>" % (self.name, self.value)
