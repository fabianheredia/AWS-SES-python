import boto3

# crear sqs cliente
sqs = boto3.client('sqs')

queue_url = '' #url de servicio sqs

# enviar cola
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