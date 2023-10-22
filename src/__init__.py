from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from src.config import Config

db = SQLAlchemy()
ma = Marshmallow()


def create_app():
    from src.views import read_blueprint, create_blueprint, update_blueprint, delete_blueprint

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app=app)

    app.register_blueprint(read_blueprint)
    app.register_blueprint(create_blueprint)
    app.register_blueprint(update_blueprint)
    app.register_blueprint(delete_blueprint)

    return app
