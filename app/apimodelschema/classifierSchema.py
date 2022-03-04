from marshmallow import Schema, fields, post_load
from app import apimodels

class ClassifierSchema(Schema):
    id = fields.Int(data_key="id")
    model_id = fields.Int(data_key="modelId")
    name = fields.String(data_key="name")
    heavy_defect_count = fields.Int(data_key="heavyDefectCount")
    light_defect_count = fields.Int(data_key="lightDefectCount")
    no_heart_count = fields.Int(data_key="noHeartCount")
    has_heart_count = fields.Int(data_key="hasHeartCount")
    undefined_count = fields.Int(data_key="undefinedCount")

    @post_load
    def make_req(self, data,**kwargs):
        return apimodels.ClassifierReq(**data)