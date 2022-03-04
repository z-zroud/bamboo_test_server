from marshmallow import Schema, fields, post_load
from app import apimodels


class LightDefectDistributionSchema(Schema):
    classifier_id = fields.Int(data_key="classifierId")
    real_light_defect_count = fields.Int(data_key="realLightDefectCount")
    heavy_defect_to_light_defect_count = fields.Int(data_key="heavyDefectToLightDefectCount")
    ok_to_light_defect_count = fields.Int(data_key="okToLightDefectCount")


    @post_load
    def make_req(self, data,**kwargs):
        return apimodels.LightDefectDistributionReq(**data)


class UndefinedDistributionSchema(Schema):
    classifier_id = fields.String(data_key="classifierId")
    real_undefined_count = fields.Float(data_key="realUndefinedCount")
    light_defect_to_undefined_count = fields.Bool(data_key="lightDefectToUndefinedCount")
    light_defect_to_ok_to_undefined_count = fields.Float(data_key="lightDefectToOKToUndefinedCount")
    ok_to_undefined_count = fields.Float(data_key="okToUndefinedCount")

    @post_load
    def make_req(self, data,**kwargs):
        return apimodels.UndefinedDistributionReq(**data)