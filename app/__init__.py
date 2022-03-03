from flask import Flask
from app.plugin import db


def create_app(app_config=None):
    app = Flask(__name__)
    app.config.from_object(app_config)
    db.init_app(app)

    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app