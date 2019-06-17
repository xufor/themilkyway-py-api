import time
from flask import request
from flask_restful import Resource
from flask_jwt_extended import (
    get_jti
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
    @classmethod
    def get(cls):
        # SAT stands for sign out access token
        # SRT stands for sign out refresh token
        # Both of these headers need to be present in the request
        sat = request.headers.get('SAT')
        srt = request.headers.get('SRT')
        # Creating blacklist objects
        sat_blacklist_object = blacklist_schema.load({'jti': get_jti(sat)}, db.session)
        srt_blacklist_object = blacklist_schema.load({'jti': get_jti(srt)}, db.session)
        # Adding a time field to all objects
        current_time = time.asctime(time.localtime(time.time()))
        sat_blacklist_object.time = current_time
        srt_blacklist_object.time = current_time
        # Adding multiple blacklisted jti to database
        if sat_blacklist_object.blacklist_token() == ERROR_WRITING_BLACKLIST_TABLE:
            return {'message': SIGN_OUT_UNSUCCESSFUL}
        else:
            srt_blacklist_object.blacklist_token()
        return {'message': SIGN_OUT_SUCCESSFUL}
