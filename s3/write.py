import boto3
s3 = boto3.resource('s3')

BUCKET_NAME = 'nichiji-tmp'
OBJECT_KEY_NAME = 'nichiji.txt'
obj = s3.Object(BUCKET_NAME,OBJECT_KEY_NAME)

date = key + '20161115\n'
obj.put(Body = date)

print(obj.get()['Body'].read().decode('utf-8'))
