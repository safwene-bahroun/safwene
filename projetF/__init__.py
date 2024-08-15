from flask import Flask
from flask_cors import CORS
from flask_session import Session
import os
from .db import init_app

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    
    # Load configuration from environment variables
    app.config.from_mapping(
        SECRET_KEY='dev',
        DB_HOST=os.getenv('DB_HOST', 'localhost'),
        DB_NAME=os.getenv('DB_NAME', 'bahroun'),
        DB_USER=os.getenv('DB_USER', 'safwene'),
        DB_PASSWORD=os.getenv('DB_PASSWORD', 'saf'),
        SESSION_TYPE='filesystem'
    )
    app.secret_key = os.urandom(24)
    init_app(app)
    from . import auth, absences
    app.register_blueprint(auth.bp)
    app.register_blueprint(absences.bp)
    
    CORS(app)
    Session(app)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

