from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Resource, Api, reqparse

class Config(object):
    SECRET_KEY = 'romko'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/text2'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)

from prog_api import models2

class Main(Resource):
    def get(self):
        q = models2.Art.query.all()
        d = []
        for qi in q:
            d += [{"title": str(qi.title), "url_article": "http://127.0.0.1:5000/" + str(qi.ids), "id": qi.ids}]
        return list(d)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("title", location = 'json')
        parser.add_argument("text", location = 'json')
        args = parser.parse_args()
        #print(args["title"])
        #print(args["text"])
        p = models2.Art(title=args["title"], text=args["text"])
        db.session.add(p)
        db.session.commit()
        
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument("title_update", location = 'json')
        parser.add_argument("text_update", location = 'json')
        parser.add_argument("id", location = 'json')
        args = parser.parse_args()
        #print(args["id"])
        u = models2.Art.query.get(args["id"])
        u.title = args["title_update"]
        u.text = args["text_update"]
        db.session.commit()

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id", location = 'json')
        args = parser.parse_args()
        #print(args["id"])
        ad = models2.Art.query.get(args["id"])
        db.session.delete(ad)
        db.session.commit()
        

class GetArticle(Resource):
    def get(self, ids):
        a = models2.Art.query.get(ids)
        return {'title': a.title, 'text': a.text}

api.add_resource(Main, '/')
api.add_resource(GetArticle, '/<ids>')

