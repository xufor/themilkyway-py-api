from ma import ma

from models.blacklist import BlacklistModel


class BlacklistSchema(ma.ModelSchema):
    class Meta:
        model = BlacklistModel
        dump_only = ('time',)
