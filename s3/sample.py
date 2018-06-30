import boto3
from datetime import datetime, timedelta
import time

s3 = boto3.resource('s3')
BUCKET_NAME = 'nichiji-tmp'
OBJECT_KEY_NAME = 'nichiji.txt'

obj = s3.Object(BUCKET_NAME,OBJECT_KEY_NAME)
key = obj.get()['Body'].read().decode('utf-8')


tmp_dates = key.split('\n')
tmp_dates = tmp_dates[:-1]

format_date = ''
for v in tmp_dates:
    format_date += v+'\n'

start = datetime.strptime(tmp_dates[-1], '%Y%m%d')
end = datetime.strptime('20180630', '%Y%m%d')

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

dates = dates[1:]

if len(dates) > 5:
    for v in dates[:5]:
        print(v)
        format_date+=v+'\n'


obj.put(Body = format_date)
