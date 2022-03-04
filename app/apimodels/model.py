
class ModelReq:
    def __init__(self,name :str,light_defect_thres : float, light_defect_to_undefined : bool, ok_thres : float, shape_thres : float):
        self.name = name
        self.light_defect_thres = light_defect_thres
        self.light_defect_to_undefined = light_defect_to_undefined
        self.ok_thres = ok_thres
        self.shape_thres = shape_thres


class ModelResp:
    def __init__(self,id, name, hash_name, light_defect_thres, light_defect_to_undefined,ok_thres,shape_thres) -> None:
        self.id = id
        self.name = name
        self.hash_name = hash_name
        self.light_defect_thres = light_defect_thres
        self.light_defect_to_undefined = light_defect_to_undefined
        self.ok_thres = ok_thres
        self.shape_thres = shape_thres