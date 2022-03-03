from app.plugin import db

class Classifier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=True)
    heavy_defect_count = db.Column(db.Integer)
    light_defect_count = db.Column(db.Integer)
    no_heart_count = db.Column(db.Integer)
    has_heart_count = db.Column(db.Integer)
    undefined_count = db.Column(db.Integer)

    def __init__(self, name, heavy_defect_count, light_defect_count,no_heart_count,has_heart_count, undefined_count):
        self.name = name
        self.heavy_defect_count = heavy_defect_count
        self.light_defect_count = light_defect_count
        self.no_heart_count = no_heart_count
        self.has_heart_count = has_heart_count
        self.undefined_count = undefined_count
