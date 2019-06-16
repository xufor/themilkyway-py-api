from marshmallow import Schema, fields


class ApproveSchema(Schema):
    sid = fields.String(required=True, validate=lambda sid: len(sid) == 8)
