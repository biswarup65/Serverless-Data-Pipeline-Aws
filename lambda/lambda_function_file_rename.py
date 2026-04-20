import json
import boto3
import urllib.parse

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Extract bucket and object key from event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])

    # Only process .gz files
    if not key.endswith('.gz'):
        return {
            'statusCode': 200,
            'body': 'Not a .gz file, skipping'
        }

    # New file name
    new_key = key.replace('.gz', '.csv')

    try:
        # Copy object to new name
        s3.copy_object(
            Bucket=bucket,
            CopySource={'Bucket': bucket, 'Key': key},
            Key=new_key
        )

        # Delete original file
        s3.delete_object(
            Bucket=bucket,
            Key=key
        )

        return {
            'statusCode': 200,
            'body': f'Renamed {key} to {new_key}'
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }