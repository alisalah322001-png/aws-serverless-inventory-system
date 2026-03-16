import boto3
import json

sns = boto3.client('sns')

TOPIC_ARN = "YOUR_SNS_TOPIC"

def lambda_handler(event, context):

    message = "New inventory file processed successfully"

    sns.publish(
        TopicArn=TOPIC_ARN,
        Message=message,
        Subject="Inventory Update"
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Notification sent')
    }