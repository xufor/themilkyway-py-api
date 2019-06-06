from ma import ma
from models.inactive import InactiveModel


class InactiveSchema(ma.ModelSchema):
    class Meta:
        model = InactiveModel
