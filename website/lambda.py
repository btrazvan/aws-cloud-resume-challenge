import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    # Initialize a DynamoDB client with Boto3
    dynamodb = boto3.resource('dynamodb')

    # Specify the DynamoDB table
    table = dynamodb.Table('ViewCount')

    # Get the item ID from the Lambda function's triggering event
    # Ensure item_id is treated as a string
    item_id = event.get('id', '0')  # Default to '0' as string if not provided

    # Try to update the item in the table
    try:
        response = table.update_item(
            Key={
                'id': item_id  # Make sure 'id' is treated as a string
            },
            UpdateExpression='SET #v = #v + :inc',
            ExpressionAttributeNames={
                '#v': 'views'  # Alias for the reserved word 'views'
            },
            ExpressionAttributeValues={
                ':inc': 1
            },
            ReturnValues="UPDATED_NEW"
        )
        return response
    except ClientError as e:
        print(e.response['Error']['Message'])
        return {
            'statusCode': 400,
            'body': e.response['Error']['Message']
        }
