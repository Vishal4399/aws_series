# This lambda function code read the file form S3

import json
import boto3

def lambda_handler(event, context):
    # Initialize S3 client
    s3 = boto3.client('s3')
    
    # Define the bucket and file name
    bucket_name = 'mybucket216'
    file_key = 'annual-enterprise-survey-2023-financial-year-provisional-size-bands.csv'
    
    try:
        # Get the file from S3
        response = s3.get_object(Bucket=bucket_name, Key=file_key)
        
        # Read the file content
        file_content = response['Body'].read().decode('utf-8')
        
        # Print the file content (or process it as needed)
        print(file_content)
        
        return {
            'statusCode': 200,
            'body': json.dumps('File read successfully!')
        }
        
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': json.dumps('Error reading the file from S3')
        }
