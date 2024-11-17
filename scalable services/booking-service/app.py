# from flask import Flask, request, jsonify

# app = Flask(__name__)

# # In-memory data store for bookings
# bookings_db = {}

# # Create a new booking
# @app.route('/bookings', methods=['POST'])
# def create_booking():
#     data = request.get_json()
#     booking_id = data.get('booking_id')
#     user_id = data.get('user_id')
#     event_id = data.get('event_id')
#     seat_number = data.get('seat_number')

#     if booking_id in bookings_db:
#         return jsonify({"error": "Booking ID already exists"}), 400

#     bookings_db[booking_id] = {
#         "booking_id": booking_id,
#         "user_id": user_id,
#         "event_id": event_id,
#         "seat_number": seat_number
#     }
#     return jsonify(bookings_db[booking_id]), 201

# # Get a booking by ID
# @app.route('/bookings/<string:booking_id>', methods=['GET'])
# def get_booking(booking_id):
#     booking = bookings_db.get(booking_id)
#     if not booking:
#         return jsonify({"error": "Booking not found"}), 404
#     return jsonify(booking), 200

# # Update a booking by ID
# @app.route('/bookings/<string:booking_id>', methods=['PUT'])
# def update_booking(booking_id):
#     booking = bookings_db.get(booking_id)
#     if not booking:
#         return jsonify({"error": "Booking not found"}), 404

#     data = request.get_json()
#     booking['user_id'] = data.get('user_id', booking['user_id'])
#     booking['event_id'] = data.get('event_id', booking['event_id'])
#     booking['seat_number'] = data.get('seat_number', booking['seat_number'])
#     bookings_db[booking_id] = booking
#     return jsonify(booking), 200

# # Delete a booking by ID
# @app.route('/bookings/<string:booking_id>', methods=['DELETE'])
# def delete_booking(booking_id):
#     if booking_id not in bookings_db:
#         return jsonify({"error": "Booking not found"}), 404
#     del bookings_db[booking_id]
#     return jsonify({"message": "Booking deleted successfully"}), 200

# # List all bookings
# @app.route('/bookings', methods=['GET'])
# def list_bookings():
#     return jsonify(list(bookings_db.values())), 200

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5002)


# from booking_service import create_app

# app = create_app()

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5002)


import sys
import os

# Add the parent directory of 'booking_service' to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '')))

from booking_service import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
