import logging
import os

from flask import Flask, Blueprint
# from flask_cors import CORS

from project.api import api


def create_app(script_info=None):
    # init app
    app = Flask(__name__)

    basedir = os.path.abspath(os.path.dirname(__file__))
    logs_dir = os.path.join(basedir, 'logs')
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)
    fh = logging.FileHandler(os.path.join(logs_dir, 'app.log'))
    app.logger.addHandler(fh)

    # enable CORS
    # CORS(app)

    # init API
    blueprint = Blueprint('api', __name__)
    api.init_app(blueprint)

    from project.api.currency_converter import ns as currency_converter_ns
    api.add_namespace(currency_converter_ns)

    app.register_blueprint(blueprint)

    # shell context for flask cli
    app.shell_context_processor({'app': app})
    return app
