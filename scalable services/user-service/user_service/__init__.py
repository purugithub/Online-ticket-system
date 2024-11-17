from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configure PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:yourpassword@postgresql:5432/user_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the database
    db.init_app(app)

    # Register blueprints (delayed import to avoid circular dependency)
    with app.app_context():
        from .routes import user_routes
        app.register_blueprint(user_routes)

        # Import models to create tables
        from .models import User
        db.create_all()

    return app
