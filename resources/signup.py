from db import db
from flask_restful import Resource
from flask import request

from schemas.inactive import InactiveSchema
from models.inactive import InactiveModel

inactive_schema = InactiveSchema()


class SignUp(Resource):
    @classmethod
    def post(cls):
        incoming_data = request.get_json()
        inactive_user_object = inactive_schema.load(incoming_data, db.session)
        discovered_entry = InactiveModel.find_entry_by_email(inactive_user_object.email)

        if discovered_entry:
            print(InactiveModel.send_email(inactive_user_object.email, '12345'))

        return {'message': inactive_user_object.email}





