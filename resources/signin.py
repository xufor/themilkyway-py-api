import bcrypt
from flask import request
from flask_restful import Resource
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token
)

from models.active import ActiveModel
from schemas.inactive import InactiveSchema
from schemas.signin import SigninSchema

inactive_schema = InactiveSchema()
signin_schema = SigninSchema()

USER_NOT_REGISTERED = 'Please create an account first.'
SIGNED_IN_SUCCESSFULLY = 'Signed in successfully.'
INCORRECT_PASSWORD = 'The provided password is incorrect.'


class SignIn(Resource):
    @classmethod
    def post(cls):
        incoming_data = request.get_json()
        # The signin_schema is made using vanilla marshmallow and not
        # flask marshmallow.
        parsed_data = signin_schema.load(incoming_data)
        incoming_email = parsed_data['email']
        incoming_password = parsed_data['password']
        # After parsing the data fetch an active user with received email
        fetched_active_user = ActiveModel.find_entry_by_email(incoming_email)
        if fetched_active_user is None:
            # Return an error if the user is not present in active table
            return {'message': USER_NOT_REGISTERED}, 400
        else:
            # Encode the fetched and incoming password
            fetched_password = fetched_active_user.password.encode()
            incoming_password = incoming_password.encode()
            # Compare the fetched and incoming password
            if bcrypt.checkpw(incoming_password, fetched_password):
                access_token = create_access_token(identity=fetched_active_user.uid, fresh=True)
                refresh_token = create_refresh_token(identity=fetched_active_user.uid)
                # If equal send access token and refresh token generated
                # using the uid.
                return {'message': SIGNED_IN_SUCCESSFULLY,
                        'access token': access_token,
                        'refresh token': refresh_token
                        }, 202
            # If password is not equal the return an error string
            else:
                return {'message': INCORRECT_PASSWORD}, 400
