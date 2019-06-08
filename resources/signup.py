import bcrypt
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
INACTIVE_USER_FOUND = 'You have already registered with this email. Please confirm your email.'
INVALID_PASSWORD_LENGTH = 'The length of password cannot be greater than 72 characters.'


class SignUp(Resource):
    @classmethod
    def post(cls):
        incoming_data = request.get_json()
        if len(incoming_data['password']) > 72:
            return {'message': INVALID_PASSWORD_LENGTH}

        encoded_password = incoming_data['password'].encode()
        hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
        incoming_data['password'] = hashed_password.decode()
        inactive_user_object = inactive_schema.load(incoming_data, db.session)
        discovered_entry = InactiveModel.find_entry_by_email(inactive_user_object.email)

        if discovered_entry is None:
            email_delivery_response = InactiveModel.send_email(inactive_user_object.email)
        else:
            return {'message': INACTIVE_USER_FOUND}

        if email_delivery_response is not None:
            indicator = inactive_user_object.create_inactive_user()
            if indicator == ERROR_WRITING_INACTIVE_TABLE:
                return {'message': ERROR_REGISTERING_USER}, 500

            code_object = code_schema.load(email_delivery_response, db.session)
            indicator = code_object.create_code_entry()
            if indicator == ERROR_WRITING_CODES_TABLE:
                return {'message': ERROR_REGISTERING_USER}, 500
        else:
            return {'message': ERROR_SENDING_EMAIL}, 400

        # This return value is temporarily equal to verification code
        # and needs to be replaced later.
        return {'verification_code': email_delivery_response['code']}





