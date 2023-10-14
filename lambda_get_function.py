import boto3
import json

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket_name = 'mittra-bucket-1'
    file_key = 'text-file.txt'
    
    try:
        response = s3.get_object(Bucket=bucket_name, Key=file_key)
        file_content = response['Body'].read().decode('utf-8')
        return file_content
    except Exception as e:
        return str(e)
