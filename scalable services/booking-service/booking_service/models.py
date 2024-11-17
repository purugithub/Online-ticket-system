from . import db
from datetime import datetime
import uuid

class Booking(db.Model):
    __tablename__ = 'bookings'  # Define the table name

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = db.Column(db.String(50), nullable=False)  # Foreign key to user ID
    event_id = db.Column(db.String(50), nullable=False)
    seat_number = db.Column(db.String(10), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    @staticmethod
    def create_booking(user_id, event_id, seat_number):
        booking = Booking(user_id=user_id, event_id=event_id, seat_number=seat_number)
        db.session.add(booking)
        db.session.commit()
        return booking

    @staticmethod
    def get_booking(booking_id):
        return Booking.query.get(booking_id)

    @staticmethod
    def update_booking(booking_id, data):
        booking = Booking.get_booking(booking_id)
        if not booking:
            return None
        booking.user_id = data.get('user_id', booking.user_id)
        booking.event_id = data.get('event_id', booking.event_id)
        booking.seat_number = data.get('seat_number', booking.seat_number)
        db.session.commit()
        return booking

    @staticmethod
    def delete_booking(booking_id):
        booking = Booking.get_booking(booking_id)
        if booking:
            db.session.delete(booking)
            db.session.commit()
        return booking

    @staticmethod
    def list_bookings():
        return Booking.query.all()
