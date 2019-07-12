from marshmallow import Schema, fields


class UpdateSchema(Schema):
    password = fields.String(required=True, validate=lambda p: len(p) <= 72)
    token = fields.String(required=True)