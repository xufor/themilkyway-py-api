from flask_restful import Resource
from models.active import ActiveModel


class Test(Resource):
    @classmethod
    def get(cls):
        x = ActiveModel.query.filter_by(uid='c13ba7').first()
        return {'result': [x.followers.name for x in x.following]}
