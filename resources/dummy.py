from flask_restful import Resource

from dummy import create_dummy_data


class Dummy(Resource):
    @classmethod
    def get(cls):
        create_dummy_data()
        return {'message': 'Successfully created dummy data.'}
