from flask import Flask
from flask_config import SECRET_KEY

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY

    from .routes.champions import champions
    app.register_blueprint(champions, url_prefix='/champions')

    return app