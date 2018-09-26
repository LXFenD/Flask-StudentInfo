from marshmallow import Schema, fields


class ProSerializer(Schema):
    id = fields.Int()
    pro_name = fields.Str()


class TeaSerializer(Schema):
    id = fields.Int()
    teach_name = fields.Str()
#
