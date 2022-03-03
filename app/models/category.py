from app.plugin import db


# # 轻微不良里面的分布情况
# self.stat_dict["real_light_defect"] = 0
# self.stat_dict["heavy_defect_to_light_defect"] = 0
# self.stat_dict["ok_to_light_defect"] = 0
# # 无法识别里面的分布情况
# self.stat_dict["real_unknown"] = 0
# self.stat_dict["light_defect_to_unknown"] = 0
# self.stat_dict["light_defect_to_ok_to_unknown"] = 0
# self.stat_dict["ok_to_unknown"] = 0

class LightDefectCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
