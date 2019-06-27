from flask import Flask
from . import routes

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')
    routes.init_app(app)
    return app