from devmgr.extensions import db


class Annotation(db.Model):
    """Key-value annotations for any config object. Annotated value is usually a json blob
    that is not indexed
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    value = db.Column(db.Binary)

    def __repr__(self):
        return '<Annotation %s>' % self.name
