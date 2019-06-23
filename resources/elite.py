from flask_jwt_extended import (
    jwt_required
)
from flask_restful import Resource

from models.active import ActiveModel

NO_IMAGE_AVAILABLE = 'No Image available.'


class Elite(Resource):
    @jwt_required
    def get(self):
        return {
            'users': [
                {
                    'image': elite_user.basic.image
                    if (elite_user.basic and elite_user.basic.image is not 'no-image')
                    else NO_IMAGE_AVAILABLE,
                    'name': elite_user.name,
                    'uid': elite_user.uid
                } for elite_user in ActiveModel.generate_elite_users()
            ]
        }









