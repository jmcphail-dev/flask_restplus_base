from flask import Flask
from app.config import config_names
from app.api import blueprint as api

def create_app(config_name=None):
    app = Flask(__name__)

    # Apply configuration
    config = config_names.get(config_name, config_names['dev'])
    app.config.from_object(config)

    # Register blueprints
    app.register_blueprint(api)

    return app