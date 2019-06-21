from ma import ma
from models.like import LikeModel


class LikeSchema(ma.ModelSchema):
    class Meta:
        include_fk = True
        model = LikeModel
        dump_only = ('time', 'source', 'sno')
