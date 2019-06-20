from marshmallow import Schema, fields


class ConfirmSchema(Schema):
    code = fields.String(required=True, validate=lambda c: len(c) == 64)
