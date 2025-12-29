from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    db.init_app(app)
    
    # Register blueprints
    from app.routes.authority_routes import authority_bp
    app.register_blueprint(authority_bp, url_prefix='/app/v1/users')
    
    return app

