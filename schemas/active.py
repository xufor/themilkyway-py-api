from ma import ma
from models.active import ActiveModel


class ActiveSchema(ma.ModelSchema):
    class Meta:
        model = ActiveModel

