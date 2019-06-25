from marshmallow import Schema, fields

from models.stories import StoryModel
from resources.profile import genres


class EditSchema(Schema):
    sid = fields.String(required=True, validate=lambda c: len(c) == 8)
    story = fields.String(required=True, validate=lambda c: StoryModel.words_counter(c) <= 10000)
    summary = fields.String(required=True, validate=lambda c: StoryModel.words_counter(c) <= 80)
    title = fields.String(required=True, validate=lambda c: StoryModel.words_counter(c) <= 10)
    genre = fields.String(required=True, validate=lambda c: len(c.split(',')) <= 3 and set(c.split(',')).issubset(set(genres)))
