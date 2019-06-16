from flask_restful import Resource

from admin import create_admin_user


class Admin(Resource):
    @classmethod
    def get(cls):
        create_admin_user()
        return {'message': 'Successfully created an admin user.'}
