from ma import ma
from models.likes import LikesModel


class LikeSchema(ma.ModelSchema):
    class Meta:
        include_fk = True
        model = LikesModel
        dump_only = ('time', 'source', 'sno')
