from flask import Blueprint, request, jsonify
from app import db
from app.models.authority_model import Authority
from app.validators.authority_validator import validate_authority_create

authority_bp = Blueprint('authority', __name__)


@authority_bp.route('/authority', methods=['POST'])
def create_authority():
    """
    Create a new authority record.
    
    Required fields:
    - name (string): The name of the authority
    
    Optional fields:
    - description (string): Description of the authority
    """
    data = request.get_json()
    
    # Validate the request data
    is_valid, error_response, status_code = validate_authority_create(data)
    if not is_valid:
        return error_response, status_code
    
    try:
        # Create new authority
        authority = Authority(
            name=data['name'].strip(),
            description=data.get('description', '').strip() if data.get('description') else None
        )
        
        db.session.add(authority)
        db.session.commit()
        
        return jsonify({
            'message': 'Authority created successfully',
            'data': authority.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'error': 'Internal Server Error',
            'message': 'Failed to create authority',
            'details': str(e)
        }), 500


@authority_bp.route('/authority', methods=['GET'])
def get_authorities():
    """
    Get all authority records.
    """
    try:
        authorities = Authority.query.all()
        return jsonify({
            'message': 'Authorities retrieved successfully',
            'data': [authority.to_dict() for authority in authorities],
            'count': len(authorities)
        }), 200
    except Exception as e:
        return jsonify({
            'error': 'Internal Server Error',
            'message': 'Failed to retrieve authorities',
            'details': str(e)
        }), 500


@authority_bp.route('/authority/<int:authority_id>', methods=['GET'])
def get_authority(authority_id):
    """
    Get a specific authority by ID.
    """
    try:
        authority = Authority.query.get_or_404(authority_id)
        return jsonify({
            'message': 'Authority retrieved successfully',
            'data': authority.to_dict()
        }), 200
    except Exception as e:
        return jsonify({
            'error': 'Not Found',
            'message': f'Authority with ID {authority_id} not found',
            'details': str(e)
        }), 404

