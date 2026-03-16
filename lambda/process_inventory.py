import json
import boto3
import csv

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('InventoryTable')

def lambda_handler(event, context):

    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    file = s3.get_object(Bucket=bucket, Key=key)

    contents = file['Body'].read().decode('utf-8').splitlines()

    reader = csv.DictReader(contents)

    for row in reader:
        table.put_item(
            Item={
                'product_id': row['product_id'],
                'name': row['name'],
                'quantity': int(row['quantity'])
            }
        )

    return {
        'statusCode': 200,
        'body': json.dumps('Inventory processed')
    }