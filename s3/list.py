import boto3
import pandas as pd
import pandas_redshift as pr
from datetime import datetime, date, timedelta
from boto3 import Session
import os
import io
import time


s3client = Session().client('s3')
start = datetime.strptime("20170101", '%Y%m%d')
end = datetime.strptime("20170201", '%Y%m%d')

def cleansing_format_data(date):
    response = s3client.list_objects(
        Bucket='ld-rawdata',
        Prefix= 'TR_JISSEKI/' + date + 'XXXXXX/'
    )

    if 'Contents' in response:
        keys = [content['Key'] for content in response['Contents']]
        key = keys[-1] #２３時のデータ

    bucket_name = 'ld-rawdata'
    file_name = key
    print(file_name)

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

for v in dates:
  cleansing_format_data(v)
  time.sleep(1)


