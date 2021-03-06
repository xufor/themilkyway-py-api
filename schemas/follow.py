from ma import ma
from models.follow import FollowModel


class FollowSchema(ma.ModelSchema):
    class Meta:
        include_fk = True
        model = FollowModel
        dump_only = ('time', 'source', 'sno')
