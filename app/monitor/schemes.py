from typing_extensions import Required
from marshmallow import Schema, fields


class CPUInfoListSchemaRequest(Schema):
    count = fields.Int(required=True)

class CPUInfoStartAcquireRequest(Schema):
    period = fields.Int(required=True)


class CPUInfoSchema(Schema):
    datetime = fields.DateTime(required=True)
    temperature = fields.Float(required=True)
    workload = fields.Float(required=True)
    frequency = fields.Float(required=True)