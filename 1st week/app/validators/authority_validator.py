from flask import jsonify


def validate_authority_create(data):
    """
    Validate authority creation data.
    Returns (is_valid, error_response) tuple.
    """
    if not data:
        return False, jsonify({
            'error': 'Validation Error',
            'message': 'Request body is required',
            'details': 'No data provided in the request body'
        }), 400
    
    required_fields = ['name']
    missing_fields = [field for field in required_fields if field not in data or not data[field]]
    
    if missing_fields:
        return False, jsonify({
            'error': 'Validation Error',
            'message': 'Missing required fields',
            'details': f'The following required fields are missing or empty: {", ".join(missing_fields)}',
            'missing_fields': missing_fields
        }), 400
    
    # Additional validation
    if 'name' in data and not isinstance(data['name'], str):
        return False, jsonify({
            'error': 'Validation Error',
            'message': 'Invalid field type',
            'details': 'Field "name" must be a string'
        }), 400
    
    if 'name' in data and len(data['name'].strip()) == 0:
        return False, jsonify({
            'error': 'Validation Error',
            'message': 'Invalid field value',
            'details': 'Field "name" cannot be empty'
        }), 400
    
    return True, None, None

