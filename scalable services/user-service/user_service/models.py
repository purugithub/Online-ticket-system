from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import uuid

# Import db only when the app context is active
from . import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    @staticmethod
    def create_user(name, email):
        new_user = User(name=name, email=email)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @staticmethod
    def get_user(user_id):
        return User.query.get(user_id)

    @staticmethod
    def update_user(user_id, data):
        user = User.get_user(user_id)
        if not user:
            return None
        user.name = data.get('name', user.name)
        user.email = data.get('email', user.email)
        db.session.commit()
        return user

    @staticmethod
    def delete_user(user_id):
        user = User.get_user(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
        return user

    @staticmethod
    def list_users():
        return User.query.all()
