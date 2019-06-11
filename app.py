import os
from flask import Flask, jsonify
from flask_restful import Api
from marshmallow import ValidationError

from db import db
from ma import ma
from resources.signup import SignUp
from resources.confirm import Confirm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

api = Api(app)
db.init_app(app)

api.add_resource(SignUp, '/signup')
api.add_resource(Confirm, '/confirm')


@app.errorhandler(ValidationError)
def handle_marshmallow_validation(err):
    return jsonify(err.messages), 400


if __name__ == '__main__':
    ma.init_app(app)
    app.run(port=5000, debug=True)
