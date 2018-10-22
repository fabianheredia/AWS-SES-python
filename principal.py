import boto3

# Create SQS client
sqs = boto3.client('sqs')

queue_url = 'https://sqs.us-east-1.amazonaws.com/654012118861/fabian1234'

# Send message to SQS queue
response = sqs.send_message(
    QueueUrl=queue_url,
    DelaySeconds=10,
    MessageAttributes={
        'Videoid': {
            'DataType': 'String',
            'StringValue': 'videoXXXX'
        },
        'rutavideo': {
            'DataType': 'String',
            'StringValue': 'ruta s3'
        }
    },
    MessageBody=(
        'Information about current NY Times fiction bestseller for '
        'week of 12/11/2016.'
    )
)

print(response['MessageId'])