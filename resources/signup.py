from db import db
from flask_restful import Resource
from flask import request

from schemas.inactive import InactiveSchema
from models.codes import ERROR_WRITING_CODES_TABLE
from schemas.codes import CodeSchema
from models.inactive import (
    InactiveModel,
    ERROR_WRITING_INACTIVE_TABLE
)

inactive_schema = InactiveSchema()
code_schema = CodeSchema()
ERROR_REGISTERING_USER = 'There was an error in registering the user.'
ERROR_SENDING_EMAIL = 'There was some error in sending confirmation e-mail.'


class SignUp(Resource):
    @classmethod
    def post(cls):
        incoming_data = request.get_json()
        inactive_user_object = inactive_schema.load(incoming_data, db.session)
        discovered_entry = InactiveModel.find_entry_by_email(inactive_user_object.email)

        email_delivery_response = None
        if discovered_entry is None:
            email_delivery_response = InactiveModel.send_email(inactive_user_object.email)

        if email_delivery_response is not None:
            write_success_indicator = inactive_user_object.create_inactive_user()
            if write_success_indicator == ERROR_WRITING_INACTIVE_TABLE:
                return {'message': ERROR_REGISTERING_USER}, 500

            code_object = code_schema.load(email_delivery_response, db.session)
            write_success_indicator = code_object.create_new_entry()
            if write_success_indicator == ERROR_WRITING_CODES_TABLE:
                return {'message': ERROR_REGISTERING_USER}, 500
        else:
            return {'message': ERROR_SENDING_EMAIL}, 400

        # This return value is temporarily equal to verification code
        # and needs to be replaced later.
        return {'message': email_delivery_response['code']}





