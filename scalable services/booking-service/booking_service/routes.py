from flask import Blueprint, request, jsonify
from .models import Booking
from .utils import validate_booking_data

booking_routes = Blueprint('booking_routes', __name__)

# Create a new booking
@booking_routes.route('/bookings', methods=['POST'])
def create_booking():
    data = request.get_json()
    validation_error = validate_booking_data(data)
    if validation_error:
        return jsonify({"error": validation_error}), 400

    user_id = data['user_id']
    event_id = data['event_id']
    seat_number = data['seat_number']

    booking = Booking.create_booking(user_id, event_id, seat_number)
    return jsonify({
        "id": booking.id,
        "user_id": booking.user_id,
        "event_id": booking.event_id,
        "seat_number": booking.seat_number,
        "created_at": booking.created_at
    }), 201

# Get a booking by ID
@booking_routes.route('/bookings/<string:booking_id>', methods=['GET'])
def get_booking(booking_id):
    booking = Booking.get_booking(booking_id)
    if not booking:
        return jsonify({"error": "Booking not found"}), 404
    return jsonify({
        "id": booking.id,
        "user_id": booking.user_id,
        "event_id": booking.event_id,
        "seat_number": booking.seat_number,
        "created_at": booking.created_at
    }), 200

# Update a booking by ID
@booking_routes.route('/bookings/<string:booking_id>', methods=['PUT'])
def update_booking(booking_id):
    booking = Booking.get_booking(booking_id)
    if not booking:
        return jsonify({"error": "Booking not found"}), 404

    data = request.get_json()
    updated_booking = Booking.update_booking(booking_id, data)
    return jsonify({
        "id": updated_booking.id,
        "user_id": updated_booking.user_id,
        "event_id": updated_booking.event_id,
        "seat_number": updated_booking.seat_number,
        "created_at": updated_booking.created_at
    }), 200

# Delete a booking by ID
@booking_routes.route('/bookings/<string:booking_id>', methods=['DELETE'])
def delete_booking(booking_id):
    booking = Booking.get_booking(booking_id)
    if not booking:
        return jsonify({"error": "Booking not found"}), 404

    Booking.delete_booking(booking_id)
    return jsonify({"message": "Booking deleted successfully"}), 200

# List all bookings
@booking_routes.route('/bookings', methods=['GET'])
def list_bookings():
    bookings = Booking.list_bookings()
    return jsonify([
        {
            "id": booking.id,
            "user_id": booking.user_id,
            "event_id": booking.event_id,
            "seat_number": booking.seat_number,
            "created_at": booking.created_at
        }
        for booking in bookings
    ]), 200
