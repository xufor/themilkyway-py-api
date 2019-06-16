from ma import ma
from models.stories import StoryModel


class StorySchema(ma.ModelSchema):
    class Meta:
        model = StoryModel
        dump_only = ('uid', 'sid', 'time', 'likes', 'reads', 'status')
