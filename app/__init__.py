from flask import Flask
from app.plugin import db,migrate

from app.models.model import Model
from app.models.classifier import Classifier
from app.models.distribution import LightDefectDistribution, UndefinedDistribution

def create_app(app_config=None):
    app = Flask(__name__)
    # app.config.from_object(app_config)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://lijie:123456@192.168.0.127/bamboo'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    migrate.init_app(app, db)
    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app