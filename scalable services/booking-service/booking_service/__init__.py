from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Use the same database as the user-service
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:yourpassword@postgresql:5432/user_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Register the booking routes
    from .routes import booking_routes
    app.register_blueprint(booking_routes)

    # Create tables if they don't exist
    with app.app_context():
        db.create_all()

    return app
