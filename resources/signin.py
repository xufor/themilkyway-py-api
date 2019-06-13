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
        parsed_data = signin_schema.load(incoming_data)
        incoming_email = parsed_data['email']
        incoming_password = parsed_data['password']
        fetched_active_user = ActiveModel.find_entry_by_email(incoming_email)
        if fetched_active_user is None:
            return {'message': USER_NOT_REGISTERED}
        else:
            fetched_password = fetched_active_user.password.encode()
            incoming_password = incoming_password.encode()
            if bcrypt.checkpw(incoming_password, fetched_password):
                access_token = create_access_token(identity=fetched_active_user.uid, fresh=True)
                refresh_token = create_refresh_token(identity=fetched_active_user.uid)

                return {'message': SIGNED_IN_SUCCESSFULLY,
                        'access token': access_token,
                        'refresh token': refresh_token
                        }, 200
            else:
                return {'message': INCORRECT_PASSWORD}
