from flask import Flask, jsonify
from flask_restful import Api
from marshmallow import ValidationError

from resources.signup import SignUp
from resources.confirm import Confirm

DB_URL = 'postgresql+psycopg2://postgres:1999@127.0.0.1:5432/themilkyway'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

api = Api(app)

api.add_resource(SignUp, '/signup')
api.add_resource(Confirm, '/confirm')


@app.errorhandler(ValidationError)
def handle_marshmallow_validation(err):
    return jsonify(err.messages), 400


if __name__ == '__main__':
    from db import db
    from ma import ma
    db.init_app(app)
    ma.init_app(app)
    app.run(port=5000, debug=True)
