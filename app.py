from flask import (
    Flask,
    jsonify
)
from flask_restful import Api
from marshmallow import ValidationError
from flask_jwt_extended import JWTManager

from db import db
from ma import ma
from resources.signup import SignUp
from resources.confirm import Confirm
from resources.signin import SignIn
from resources.signout import SignOut
from resources.submit import Submit
from resources.approve import Approve
from resources.reject import Reject
from resources.dummy import Dummy
from resources.refresh import Refresh
from resources.drop import Drop
from resources.test import Test
from resources.follow import Follow
from resources.like import Like
from resources.read import Read
from resources.search import Search
from resources.profile import Profile
from resources.elite import Elite
from models.blacklist import BlacklistModel
from dummy import UID

TOKEN_REVOKED = 'The token has been revoked. Please login again.'
TOKEN_EXPIRED = 'The token has expired. Please refresh it.'
TOKEN_INVALID = 'The token is invalid.'

DB_URL = 'postgresql+psycopg2://postgres:1999@127.0.0.1:5432/themilkyway'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

app.secret_key = 'u83bdd537e9g0yt7yvc8cm5ex9c8n9v2a'

api = Api(app)

jwt = JWTManager(app)

db.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()


@jwt.revoked_token_loader
def when_token_is_revoked():
    return jsonify({'message': TOKEN_REVOKED})


@jwt.expired_token_loader
def when_token_is_revoked():
    return jsonify({'message': TOKEN_EXPIRED})


@jwt.invalid_token_loader
def when_token_is_invalid(reason):
    return jsonify({'message': TOKEN_INVALID, 'reason': reason})


@jwt.user_claims_loader
def add_claims_to_jwt(identity):
    if identity == UID[0]:
        return {'is_admin': True}
    return {'is_admin': False}


@app.errorhandler(ValidationError)
def handle_marshmallow_validation(err):
    return jsonify(err.messages), 400


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    return BlacklistModel.check_jti_in_blacklist(decrypted_token['jti'])


api.add_resource(SignUp, '/signup')
api.add_resource(SignIn, '/signin')
api.add_resource(SignOut, '/signout')
api.add_resource(Confirm, '/confirm/<string:code>')
api.add_resource(Submit, '/submit')
api.add_resource(Approve, '/approve')
api.add_resource(Reject, '/reject')
api.add_resource(Dummy, '/dummy')
api.add_resource(Refresh, '/refresh')
api.add_resource(Drop, '/drop')
api.add_resource(Test, '/test')
api.add_resource(Follow, '/follow')
api.add_resource(Like, '/like')
api.add_resource(Read, '/read')
api.add_resource(Profile, '/profile')
api.add_resource(Search, '/search')
api.add_resource(Elite, '/elite')

if __name__ == '__main__':
    ma.init_app(app)
    app.run(port=5000, debug=True)
