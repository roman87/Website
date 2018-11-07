from prog import db

class AF(db.Model):

    ids = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    article = db.Column(db.String(2048))
    comments = db.relationship('Comment', backref='article', lazy='dynamic')

    def __repr__(self):
        return self.title

class Comment(db.Model):

    ids = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    comment = db.Column(db.String(512))
    art_id = db.Column(db.Integer, db.ForeignKey('AF.ids'))

    def __repr__(self):
        return self.name
