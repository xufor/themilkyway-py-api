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

        if discovered_entry is not None:
            print(InactiveModel.send_email(inactive_user_object.email, '12345'))

        return {'message': inactive_user_object.email}


class SaveInactive(Resource):
    @classmethod
    def post(cls):
        incoming_data = request.get_json()
        inactive_user_object = inactive_schema.load(incoming_data, db.session)
        db.session.add(inactive_user_object)
        db.session.commit()
        return{"message": "save to inactive database"}




