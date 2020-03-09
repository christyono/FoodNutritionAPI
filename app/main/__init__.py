from flask import Flask
from flask_cors import CORS
from app.main.controller.user_controller import user


def _initialize_blueprints(app):
    '''
    register flask blueprints
    '''
    app.register_blueprint(user, url_prefix='/api/v1')


def create_app():
    '''
    create application by initializing components.
    '''
    app = Flask(__name__)
    CORS(app)

    _initialize_blueprints(app)

    return app
