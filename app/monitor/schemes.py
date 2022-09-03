from typing_extensions import Required
from marshmallow import Schema, fields


class CPUInfoListSchemaRequest(Schema):
    count = fields.Int(required=True)

class CPUInfoStartAcquireRequest(Schema):
    period = fields.Int(required=True)


class CPUInfoSchema(Schema):
    datetime = fields.DateTime(required=True)
    temp = fields.Float(required=True)