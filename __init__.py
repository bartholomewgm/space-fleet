from flask import Flask
from app.routes.spaceship_routes import spaceship_bp
from app.routes.mission_routes import mission_bp
from app.errors import register_errors


def create_app():
    app = Flask(__name__)

    app.register_blueprint(spaceship_bp, url_prefix='/api/v1')
    app.register_blueprint(mission_bp, url_prefix='/api/v1')

    register_errors(app)

    return app
