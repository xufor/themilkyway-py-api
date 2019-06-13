from flask import Flask, jsonify
from flask_restful import Api
from marshmallow import ValidationError
from flask_jwt_extended import JWTManager

from db import db
from ma import ma
from resources.signup import SignUp
from resources.confirm import Confirm
from resources.signin import SignIn


DB_URL = 'postgresql+psycopg2://postgres:1999@127.0.0.1:5432/themilkyway'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True


jwt = JWTManager(app)
app.secret_key = 'u83bdd537e9'
api = Api(app)
db.init_app(app)

api.add_resource(SignUp, '/signup')
api.add_resource(SignIn, '/signin')
api.add_resource(Confirm, '/confirm/<string:code>')


@app.errorhandler(ValidationError)
def handle_marshmallow_validation(err):
    return jsonify(err.messages), 400


if __name__ == '__main__':
    ma.init_app(app)
    app.run(port=5000, debug=True)
