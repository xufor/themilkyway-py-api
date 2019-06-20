from flask_restful import Resource
from models.active import ActiveModel


class Test(Resource):
    @classmethod
    def get(cls):
        x = ActiveModel.query.filter_by(uid='6be2a5').first()
        print(x.submissions)
        return {'result': 'done'}
