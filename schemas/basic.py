from ma import ma
from models.basic import BasicModel


class BasicSchema(ma.ModelSchema):
    class Meta:
        model = BasicModel
        dump_only = ('sno', 'uid')
