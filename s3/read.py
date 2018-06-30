import boto3

s3 = boto3.resource('s3')

BUCKET_NAME = 'nichiji-tmp'
OBJECT_KEY_NAME = 'nichiji.txt'

obj = s3.Object(BUCKET_NAME,OBJECT_KEY_NAME)
key = obj.get()['Body'].read().decode('utf-8')

dates = key.split('\n')
dates = dates[:-1]
print(dates)
print(dates[-1])



