from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Resource, Api

class Config(object):
    SECRET_KEY = 'romko'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/text2'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)

from prog_api import models2

class Hi(Resource):
    def get(self):
        return {'hello': 'Roman'}

class GetArticle(Resource):
    def get(self, ids):
        a = models2.Art.query.get(ids)
        return {'title': a.title, 'text': a.text}

api.add_resource(Hi, '/')
api.add_resource(GetArticle, '/<ids>')

