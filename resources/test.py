import os
from flask_restful import Resource

ADMIN_UID = os.getenv('ADMIN_USER', '26e1a2')


class Test(Resource):
    @classmethod
    def get(cls):
        return {"message": ADMIN_UID == "ffffff"}
