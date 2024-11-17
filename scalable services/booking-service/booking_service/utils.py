def validate_booking_data(data):
    if not data.get('user_id'):
        return "User ID is required"
    if not data.get('event_id'):
        return "Event ID is required"
    if not data.get('seat_number'):
        return "Seat number is required"
    return None
