from marshmallow import Schema, fields


class ProfileSchema(Schema):
    uid = fields.String(required=True, validate=lambda u: len(u) == 6)
