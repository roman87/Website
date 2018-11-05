from prog import db

class AF(db.Model):

    ids = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    article = db.Column(db.String(2048))

    def __repr__(self):
        return self.title
