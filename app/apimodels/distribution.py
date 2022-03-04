
class LightDefectDistributionReq:
    def __init__(self, classifier_id, real_light_defect_count, heavy_defect_to_light_defect_count, ok_to_light_defect_count):
        self.classifier_id = classifier_id
        self.real_light_defect_count = real_light_defect_count
        self.heavy_defect_to_light_defect_count = heavy_defect_to_light_defect_count
        self.ok_to_light_defect_count = ok_to_light_defect_count

class LightDefectDistributionResp:
    def __init__(self, real_light_defect_count, heavy_defect_to_light_defect_count, ok_to_light_defect_count):
        self.real_light_defect_count = real_light_defect_count
        self.heavy_defect_to_light_defect_count = heavy_defect_to_light_defect_count
        self.ok_to_light_defect_count = ok_to_light_defect_count

class UndefinedDistributionReq:
    def __init__(self,classifier_id,real_undefined_count,light_defect_to_undefined_count,light_defect_to_ok_to_undefined_count,ok_to_undefined_count):
        self.classifier_id = classifier_id
        self.real_undefined_count = real_undefined_count
        self.light_defect_to_undefined_count = light_defect_to_undefined_count
        self.light_defect_to_ok_to_undefined_count = light_defect_to_ok_to_undefined_count
        self.ok_to_undefined_count = ok_to_undefined_count


class UndefinedDistributionResp:
    def __init__(self,real_undefined_count,light_defect_to_undefined_count,light_defect_to_ok_to_undefined_count,ok_to_undefined_count):
        self.real_undefined_count = real_undefined_count
        self.light_defect_to_undefined_count = light_defect_to_undefined_count
        self.light_defect_to_ok_to_undefined_count = light_defect_to_ok_to_undefined_count
        self.ok_to_undefined_count = ok_to_undefined_count