from flask_restful import Resource
from models.active import ActiveModel


class Test(Resource):
    @classmethod
    def get(cls):
        x = ActiveModel.query.filter_by(uid='7ui87h').first()
        return {'result': x.stories[0].story}
