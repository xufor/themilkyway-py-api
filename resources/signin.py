from flask_restful import Resource
import bcrypt
from flask import request
from models.active import ActiveModel


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
            if check_password == True:
                return {'message': 'successfully login'}
            else:
                return {'message': 'check password'}
