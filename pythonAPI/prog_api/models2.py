from prog_api import db

class Art(db.Model):

    ids = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    text = db.Column(db.String(2048))

    def __repr__(self):
        return self.title
