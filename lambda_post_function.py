import boto3
import json

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket_name = 'mittra-bucket-1'
    file_key = 'text-file.txt'
    file_content = event['body']
    
    try:
        s3.put_object(Body=file_content, Bucket=bucket_name, Key=file_key)
        return 'Erfolgreich gespeichert'
    except Exception as e:
        return str(e)
