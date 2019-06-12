from flask_restful import Resource
from db import db
from flask_jwt_extended import JWTManager
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
        signin_user_object = signin_schema.load(incoming_data, db.session)

        if ActiveModel.find_entry_by_email(signin_user_object.email) is None:
            return {'message': 'SignUp first or invalid email'}
        elif ActiveModel.find_entry_by_email(signin_user_object.email) is not None:
            database_password = ActiveModel.find_entry_by_email(signin_user_object.email).password.encode()
            encoded_password = signin_user_object.password.encode()
            check_password = bcrypt.checkpw(encoded_password, database_password)
            if check_password == True:
                return {'message': 'successfully login'}
            else:
                return {'message': 'check password'}
