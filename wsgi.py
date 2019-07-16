from ma import ma
from app import app
from flask_cors import CORS

ma.init_app(app)
CORS(app)
