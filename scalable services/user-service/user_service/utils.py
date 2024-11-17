def validate_user_data(data, require_user_id=False):
    if require_user_id and not data.get('user_id'):
        return "User ID is required"
    if not data.get('name'):
        return "Name is required"
    if not data.get('email'):
        return "Email is required"
    return None
