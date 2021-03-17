from flask import Flask
from app.controllers import inmem

def create_app(config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)

    app.register_blueprint(inmem)

    return app