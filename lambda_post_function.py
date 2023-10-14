import json
import boto3
import uuid

s3 = boto3.client('s3')
bucket_name = "mittra-bucket-1"

def lambda_handler(event, context):
    message = json.loads(event['body'])['message']
    file_name = str(uuid.uuid4()) + ".txt"
    
    s3.put_object(Body=message, Bucket=bucket_name, Key=file_name)
    
    get_url = f"https://85klnd83ad.execute-api.eu-central-1.amazonaws.com/get?file_name={file_name}"
    
    return {
        'statusCode': 200,
        'body': json.dumps({"get_url": get_url})
    }
