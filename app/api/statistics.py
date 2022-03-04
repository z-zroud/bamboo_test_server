from msilib import schema
from flask import jsonify,request
from app.api import bp
from app import apimodelschema
from app.apimodels import Response, ModelResp, ClassifierResp
from app.apimodels.distribution import LightDefectDistributionResp, UndefinedDistributionResp
from app.models.model import Model
from app.models.classifier import Classifier
from app.models.distribution import LightDefectDistribution, UndefinedDistribution
from app.plugin import db


@bp.route('/model', methods=['POST'])
def add_model():
    data = request.get_json()

    schema = apimodelschema.ModelSchema()
    ret = schema.load(data)

    model = Model(ret.name, ret.light_defect_thres, ret.light_defect_to_undefined, ret.ok_thres, ret.shape_thres)

    m = Model.query.filter_by(hash_name=model.hash_name).first()
    if m is None:
        db.session.add(model)
        db.session.commit()

    return jsonify(Response().to_dict())


@bp.route('/model', methods=['GET'])
def get_models():
    models = Model.query.all()
    rets = []
    for m in models:
        rets.append(ModelResp(m.id, m.name,m.hash_name,m.light_defect_thres, m.light_defect_to_undefined,m.ok_thres, m.shape_thres))
    schema = apimodelschema.ModelSchema(many=True)
    return jsonify(schema.dump(rets))


@bp.route('/classifier', methods=['POST'])
def add_classifier():
    data = request.get_json()

    schema = apimodelschema.ClassifierSchema()
    ret = schema.load(data)

    classifier = Classifier(ret.model_id, ret.name, ret.heavy_defect_count, ret.light_defect_count,ret.no_heart_count,ret.has_heart_count, ret.undefined_count)
    c = Classifier.query.filter_by(model_id=ret.model_id, name=ret.name).first()
    if c is None:
        db.session.add(classifier)
        db.session.commit()

    return jsonify(Response().to_dict())

@bp.route('/classifier', methods=['GET'])
def get_classifier():
    modelId = request.args.get("modelId")
    classifiers = Classifier.query.filter_by(model_id=modelId).all()
    rets = []
    for c in classifiers:
        rets.append(ClassifierResp(c.id, c.model_id, c.name, c.heavy_defect_count, c.light_defect_count, c.no_heart_count, c.has_heart_count, c.undefined_count))
    schema = apimodelschema.ClassifierSchema(many=True)
    return jsonify(schema.dump(rets))

@bp.route('/distribution/lightDefect', methods=['POST'])
def add_light_defect_distribution():
    data = request.get_json()

    schema = apimodelschema.LightDefectDistributionSchema()
    ret = schema.load(data)

    classifier = LightDefectDistribution(ret.classifier_id, ret.real_light_defect_count, ret.heavy_defect_to_light_defect_count,ret.ok_to_light_defect_count)

    db.session.add(classifier)
    db.session.commit()

    return jsonify(Response().to_dict())

@bp.route('/distribution/lightDefect', methods=['GET'])
def get_light_defect_distribution():
    classifier_id = request.args.get("classifierId")
    distributions = LightDefectDistribution.query.filter_by(classifier_id=classifier_id).all()
    rets = []
    for d in distributions:
        rets.append(LightDefectDistributionResp(d.real_light_defect_count, d.heavy_defect_to_light_defect_count, d.ok_to_light_defect_count))
    schema = apimodelschema.LightDefectDistributionSchema(many=True)
    return jsonify(schema.dump(rets))

@bp.route('/distribution/undefined', methods=['POST'])
def add_undefined_distribution():
    data = request.get_json()

    schema = apimodelschema.UndefinedDistributionSchema()
    ret = schema.load(data)

    distribution = UndefinedDistribution(ret.classifier_id, ret.real_undefined_count, ret.light_defect_to_undefined_count,ret.light_defect_to_ok_to_undefined_count,ret.ok_to_undefined_count)

    db.session.add(distribution)
    db.session.commit()

    return jsonify(Response().to_dict())

@bp.route('/distribution/undefined', methods=['GET'])
def get_undefined_distribution():
    classifier_id = request.args.get("classifierId")
    distributions = UndefinedDistribution.query.filter_by(classifier_id=classifier_id).all()
    rets = []
    for d in distributions:
        rets.append(UndefinedDistributionResp(d.real_undefined_count, d.light_defect_to_undefined_count, d.light_defect_to_ok_to_undefined_count, d.ok_to_undefined_count))
    schema = apimodelschema.UndefinedDistributionSchema(many=True)
    return jsonify(schema.dump(rets))