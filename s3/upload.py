import boto3
from datetime import datetime, timedelta
from boto3 import Session
s3client = Session().client('s3')

#bucket のなかにkeyが入っていればTrue
def exists(bucket: str, key: str) -> bool:
    contents = s3client.list_objects(Prefix=key, Bucket=bucket).get("Contents")
    if contents:
        for content in contents:
            if content.get("Key") == key:
                return True
    return False

def WriteFile(v):
    print("finished process!!!")


s3 = boto3.resource('s3')

#環境変数に直す
start_day = '20161115'
end_day = '20170101'

BUCKET_NAME = 'nichiji-tmp'
OBJECT_KEY_NAME = start_day+'_'+end_day+'.txt'

if exists(BUCKET_NAME, OBJECT_KEY_NAME) != True:
    s3.Bucket(BUCKET_NAME).put_object(Key=OBJECT_KEY_NAME)

start = datetime.strptime(start_day, '%Y%m%d')
end = datetime.strptime(end_day, '%Y%m%d')


def daterange(start_date, end_date):
    for n in range((end_date - start_date).days):
        yield start_date + timedelta(n)

dates = []
for i in daterange(start, end):
    y = str(i.year)
    m = str(i.month)
    d = str(i.day)
    if len(m) !=2:
        m = '0' + m
    if len(d) != 2:
        d = '0' + d

    dates.append(y+m+d)

obj = s3.Object(BUCKET_NAME, OBJECT_KEY_NAME)
key = obj.get()['Body'].read().decode('utf-8')
tmp_dates = key.split('\n')
tmp_dates = tmp_dates[:-1]

in_date = ''
for v in dates:
    if v in tmp_dates:
        in_date +=v+'\n'
    else:
        WriteFile(v)
        in_date+=v+'\n'
        break

obj.put(Body = in_date)

print("quit")



