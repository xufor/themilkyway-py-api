from ma import ma
from models.codes import CodeModel


class CodeSchema(ma.ModelSchema):
    class Meta:
        model = CodeModel
