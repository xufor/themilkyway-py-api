from ma import ma
from models.signin import SignInModel


class SignInSchema(ma.ModelSchema):
    class Meta:
        model = SignInModel
