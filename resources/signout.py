from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_raw_jwt
from blacklist import BLACKLIST


class SignOut(Resource):
    @classmethod
    @jwt_required
    def post(cls):
        jti = get_raw_jwt()['jti']
        BLACKLIST.add(jti)
        return {"message": "successfully signout"}
