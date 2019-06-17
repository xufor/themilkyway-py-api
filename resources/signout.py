import time
from flask_restful import Resource
from flask_jwt_extended import (
    jwt_required,
    get_raw_jwt
)

from db import db
from schemas.blacklist import BlacklistSchema
from models.blacklist import (
    ERROR_WRITING_BLACKLIST_TABLE
)

blacklist_schema = BlacklistSchema()

SIGN_OUT_SUCCESSFUL = 'Signed out successfully.'
SIGN_OUT_UNSUCCESSFUL = 'Signing out unsuccessful.'


class SignOut(Resource):
    @jwt_required
    def get(self):
        # Getting the jti from access token
        jti = get_raw_jwt()['jti']
        # Creating a blacklist object
        blacklist_object = blacklist_schema.load({'jti': jti}, db.session)
        # Adding a time field
        blacklist_object.time = time.asctime(time.localtime(time.time()))
        # Adding blacklisted jti to database
        if blacklist_object.blacklist_token() == ERROR_WRITING_BLACKLIST_TABLE:
            return {'message': SIGN_OUT_UNSUCCESSFUL}
        return {'message': SIGN_OUT_SUCCESSFUL}
