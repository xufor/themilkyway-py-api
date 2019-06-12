from flask_restful import Resource
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity
import bcrypt
from flask import request


from models.active import ActiveModel
from schemas.inactive import InactiveSchema
from schemas.signin import SignInSchema

inactive_schema = InactiveSchema()
signin_schema = SignInSchema()


class SignIn(Resource):
    @classmethod
    def post(cls):
        incoming_data = request.get_json()
        incoming_email = incoming_data['email']
        incoming_password = incoming_data['password']
        if ActiveModel.find_entry_by_email(incoming_email) is None:
            return {'message': 'SignUp first or invalid email'}
        elif ActiveModel.find_entry_by_email(incoming_email) is not None:
            signup_password = ActiveModel.find_entry_by_email(incoming_email).password.encode()
            encoded_password = incoming_password.encode()
            check_password = bcrypt.checkpw(encoded_password, signup_password)
            if check_password:
                _id = get_jwt_identity()
                access_token = create_access_token(identity=_id, fresh=True)
                refresh_token = create_refresh_token(identity=_id)

                return {'message': 'successfully login',
                        'access token': access_token,
                        'refresh token': refresh_token
                        }, 200
            else:
                return {'message': 'check password'}
