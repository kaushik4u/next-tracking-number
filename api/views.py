import random
import string
from datetime import datetime, timezone
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET'])
def get_next_tracking_number(request):
    """ 
    Extract query parameters 
    """
    origin_country_id = request.query_params.get('origin_country_id')
    destination_country_id = request.query_params.get('destination_country_id')
    weight = request.query_params.get('weight')
    created_at = request.query_params.get('created_at')
    customer_id = request.query_params.get('customer_id')
    customer_name = request.query_params.get('customer_name')
    customer_slug = request.query_params.get('customer_slug')

    """
    Generate a unique tracking number
    """
    tracking_number = generate_unique_tracking_number()

    """
    Generate RFC 3339 formatted created_at with timezone information
    """
    current_time = datetime.now(timezone.utc).astimezone().isoformat()

    """
    Prepare response data without saving to the database
    """
    response_data = {
        'tracking_number': tracking_number,
        'created_at': current_time,  # RFC 3339 formatted timestamp
        'origin_country_id': origin_country_id,
        'destination_country_id': destination_country_id,
        'customer_id': customer_id,
    }

    """
    Return the generated tracking number in the response
    """
    return Response(response_data, status=status.HTTP_200_OK)

def generate_unique_tracking_number():
    """Generate a unique tracking number."""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
