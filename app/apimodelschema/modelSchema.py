from marshmallow import Schema, fields, post_load
from app import apimodels


class ModelSchema(Schema):
    id = fields.String(data_key="id")
    name = fields.String(data_key="name")
    hash_name = fields.String(data_key="uniqueName")
    light_defect_thres = fields.Float(data_key="lightDefectThres")
    light_defect_to_undefined = fields.Bool(data_key="isLightDefectThresToUndefined")
    ok_thres = fields.Float(data_key="okThres")
    shape_thres = fields.Float(data_key="shapeThres")

    @post_load
    def make_req(self, data,**kwargs):
        return apimodels.ModelReq(**data)
