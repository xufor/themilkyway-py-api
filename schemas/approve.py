from marshmallow import Schema, fields


class ApproveSchema(Schema):
    sid = fields.String(required=True, validate=lambda s: len(s) == 8)
