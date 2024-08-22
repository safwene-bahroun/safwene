from flask import Flask
from flask_cors import CORS
import os
from .db import init_app

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        DB_HOST=os.getenv('DB_HOST', 'localhost'),
        DB_NAME=os.getenv('DB_NAME', 'bahroun'),
        DB_USER=os.getenv('DB_USER', 'safwene'),
        DB_PASSWORD=os.getenv('DB_PASSWORD', 'saf'),
    )
    init_app(app)

    from .auth import init_auth_routes
    from .absences import init_absences_routes
    init_auth_routes(app)
    init_absences_routes(app)
    CORS(app)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
