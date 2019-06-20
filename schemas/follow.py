from ma import ma
from models.follow import FollowModel


class FollowSchema(ma.ModelSchema):
    class Meta:
        model = FollowModel
        dump_only = ('time', 'uid', 'sno')
