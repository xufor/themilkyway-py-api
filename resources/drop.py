from flask_restful import Resource

from drop import drop_all_tables


class Drop(Resource):
    @classmethod
    def get(cls):
        drop_all_tables()
        return {'message': 'Successfully dropped all tables.'}