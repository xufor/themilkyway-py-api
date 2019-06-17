from flask_restful import Resource
from flask_jwt_extended import (
    create_access_token,
    jwt_refresh_token_required,
    get_jwt_identity,
)


class Refresh(Resource):
    @jwt_refresh_token_required
    def get(self):
        refreshed_access_token = create_access_token(identity=get_jwt_identity(), fresh=False)
        return {'access_token': refreshed_access_token}, 200
