
class ClassifierReq:
    def __init__(self,model_id, name, heavy_defect_count, light_defect_count,no_heart_count,has_heart_count,undefined_count):
        self.model_id = model_id
        self.name = name
        self.heavy_defect_count = heavy_defect_count
        self.light_defect_count = light_defect_count
        self.no_heart_count = no_heart_count
        self.has_heart_count = has_heart_count
        self.undefined_count = undefined_count


class ClassifierResp:
    def __init__(self,id, model_id, name, heavy_defect_count, light_defect_count,no_heart_count,has_heart_count,undefined_count):
        self.id = id
        self.model_id = model_id
        self.name = name
        self.heavy_defect_count = heavy_defect_count
        self.light_defect_count = light_defect_count
        self.no_heart_count = no_heart_count
        self.has_heart_count = has_heart_count
        self.undefined_count = undefined_count