from app.plugin import db

class LightDefectDistribution(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    real_light_defect_count = db.Column(db.Integer)
    heavy_defect_to_light_defect_count = db.Column(db.Integer)
    ok_to_light_defect = db.Column(db.Integer)

    classifier_id = db.Column(db.Integer, db.ForeignKey("classifier.id"))

    def __init__(self, classifier_id, real_light_defect_count, heavy_defect_to_light_defect_count, ok_to_light_defect):
        self.classifier_id = classifier_id
        self.real_light_defect_count = real_light_defect_count
        self.heavy_defect_to_light_defect_count = heavy_defect_to_light_defect_count
        self.ok_to_light_defect = ok_to_light_defect


class UndefinedDistribution(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    real_undefined_count = db.Column(db.Integer)
    light_defect_to_undefined_count = db.Column(db.Integer)
    light_defect_to_ok_to_undefined_count = db.Column(db.Integer)
    ok_to_undefined_count = db.Column(db.Integer)

    classifier_id = db.Column(db.Integer, db.ForeignKey("classifier.id"))

    def __init__(self, classifier_id, real_undefined_count,light_defect_to_undefined_count,light_defect_to_ok_to_undefined_count,ok_to_undefined_count):
        self.classifier_id = classifier_id
        self.real_undefined_count = real_undefined_count
        self.light_defect_to_undefined_count = light_defect_to_undefined_count
        self.light_defect_to_ok_to_undefined_count = light_defect_to_ok_to_undefined_count
        self.ok_to_undefined_count = ok_to_undefined_count


