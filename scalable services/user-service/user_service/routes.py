from flask import Blueprint, request, jsonify
from .models import User
from .utils import validate_user_data

user_routes = Blueprint('user_routes', __name__)

# Create a new user

@user_routes.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    validation_error = validate_user_data(data)  # Don't require user_id for POST
    if validation_error:
        return jsonify({"error": validation_error}), 400

    user = User.create_user(data['name'], data['email'])
    return jsonify({
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "created_at": user.created_at
    }), 201
