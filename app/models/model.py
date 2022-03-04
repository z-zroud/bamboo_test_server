from app.plugin import db


class Model(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    hash_name = db.Column(db.String(128), nullable=False, unique=True)
    light_defect_thres = db.Column(db.Float, nullable=False)
    light_defect_to_undefined = db.Column(db.Boolean, nullable=False)
    ok_thres = db.Column(db.Float, nullable=False)
    shape_thres = db.Column(db.Float, nullable=False)

    classifiers = db.relationship('Classifier', backref='model')

    def __init__(self, name, light_defects_thres, light_defect_to_undefined, ok_thres, shape_thres=0.9):
        self.name = name
        self.light_defect_thres = light_defects_thres
        self.light_defect_to_undefined = light_defect_to_undefined
        self.ok_thres = ok_thres
        self.shape_thres = shape_thres
        self.hash_name = f'{name}-{light_defects_thres}-{light_defect_to_undefined}-{ok_thres}-{shape_thres}'

