import json
import boto3

s3 = boto3.client('s3')
bucket_name = "mittra-bucket-1"

def lambda_handler(event, context):
    file_name = event['queryStringParameters']['file_name']
    
    try:
        obj = s3.get_object(Bucket=bucket_name, Key=file_name)
        text = obj['Body'].read().decode('utf-8')
        
        s3.delete_object(Bucket=bucket_name, Key=file_name)
        
        return {
            'statusCode': 200,
            'body': json.dumps({"message": text})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({"error": str(e)})
        }
