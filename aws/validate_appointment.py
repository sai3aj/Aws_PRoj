def lambda_handler(event, context):
    appointment_data = event['appointment_data']
    
    # Validation logic
    if 'appointment_id' not in appointment_data or 'user_email' not in appointment_data:
        return {'statusCode': 400, 'message': 'Invalid data'}

    return {'statusCode': 200, 'message': 'Validation successful'}
