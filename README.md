# AWS Serverless Inventory System

This project demonstrates a serverless architecture on AWS.

## Architecture

User uploads inventory file → S3 → Lambda → DynamoDB → Lambda → SNS → Email

## AWS Services Used

S3
Lambda
DynamoDB
SNS
Cognito

## Workflow

1. Upload CSV inventory file
2. S3 triggers Lambda
3. Lambda processes CSV
4. Data stored in DynamoDB
5. SNS sends notification

## Author

Ali Salah