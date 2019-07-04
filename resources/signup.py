import time
import bcrypt
from db import db
from flask_restful import Resource
from flask import request

from models.active import ActiveModel
from models.inactive import (
    InactiveModel,
    ERROR_WRITING_INACTIVE_TABLE
)
from schemas.inactive import InactiveSchema

inactive_schema = InactiveSchema()

ERROR_REGISTERING_USER = 'There was an error in registering the user.'
ERROR_SENDING_EMAIL = 'There was some error in sending confirmation e-mail.'
INACTIVE_USER_FOUND = 'There is an inactive user already registered with this email.'
ACTIVE_USER_FOUND = 'There is an active user already registered with this email.'
INVALID_PASSWORD_LENGTH = 'The length of password cannot be greater than 72 characters.'


class SignUp(Resource):
    @classmethod
    def post(cls):
        inactive_user_object = inactive_schema.load(request.get_json(), db.session)

        if ActiveModel.find_entry_by_email(inactive_user_object.email) is not None:
            return {'message': ACTIVE_USER_FOUND}, 400

        if InactiveModel.find_entry_by_email(inactive_user_object.email) is None:
            email_delivery_response = InactiveModel.send_email(inactive_user_object.email)
        else:
            return {'message': INACTIVE_USER_FOUND}, 400

        # Checking if email was successfully sent or not
        if email_delivery_response is not None:
            # Checking password length and hashing it
            if len(inactive_user_object.password) > 72:
                return {'message': INVALID_PASSWORD_LENGTH}, 400

            encoded_password = inactive_user_object.password.encode()
            hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
            inactive_user_object.password = hashed_password.decode()

            # Adding a code field after generating a fresh code
            inactive_user_object.code = email_delivery_response['code']

            # Adding the time field using the inbuilt python module
            inactive_user_object.time = time.asctime(time.gmtime(time.time()))

            # Creating inactive user and checking if the operation was
            # successful or not.
            if inactive_user_object.create_inactive_user() == ERROR_WRITING_INACTIVE_TABLE:
                return {
                           'message': ERROR_REGISTERING_USER,
                           'details': ERROR_WRITING_INACTIVE_TABLE
                       }, 500
        else:
            return {'message': ERROR_SENDING_EMAIL}, 400

        # This return value is temporarily equal to verification code
        # and needs to be replaced later.
        return {
            'confirmation_link': 'http://127.0.0.1:5000/confirm/{}'.format(email_delivery_response['code']),
            'message': 'Operation successful.'
        }





