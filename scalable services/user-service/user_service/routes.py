from flask import Blueprint, request, jsonify
from .models import User
from .utils import validate_user_data  # You can add a utility function to validate user input if necessary

user_routes = Blueprint('user_routes', __name__)

# Route to create a new user (POST)
@user_routes.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    # You can add your validation logic here if you have a function like `validate_user_data`
    validation_error = validate_user_data(data)  # Optional validation function
    if validation_error:
        return jsonify({"error": validation_error}), 400

    user = User.create_user(data['name'], data['email'])
    return jsonify({
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "created_at": user.created_at
    }), 201

# Route to get all users (GET)
@user_routes.route('/users', methods=['GET'])
def get_users():
    users = User.list_users()
    return jsonify([{
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "created_at": user.created_at
    } for user in users])

# Route to get a single user by ID (GET)
@user_routes.route('/users/<string:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.get_user(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify({
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "created_at": user.created_at
    })

# Route to update an existing user (PUT)
@user_routes.route('/users/<string:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.get_user(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    updated_user = User.update_user(user_id, data)
    if not updated_user:
        return jsonify({"error": "Failed to update user"}), 400

    return jsonify({
        "id": updated_user.id,
        "name": updated_user.name,
        "email": updated_user.email,
        "created_at": updated_user.created_at
    })

# Route to delete a user (DELETE)
@user_routes.route('/users/<string:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.get_user(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    deleted_user = User.delete_user(user_id)
    return jsonify({
        "message": f"User {deleted_user.name} deleted successfully"
    })
