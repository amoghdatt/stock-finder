from django.conf import settings
import requests
from datetime import datetime
from celery import shared_task
from zipfile import ZipFile
import csv
from io import BytesIO, StringIO
import os
import re
import json
import redis
from django.conf import settings


@shared_task
def download_equity_bhavcopy_zip(date_string=None):

    print('Executing download task.....')


    # connect redis
    redis_instance = redis.StrictRedis(host = settings.REDIS_HOST, port=settings.REDIS_PORT, password=settings.REDIS_PASSWORD, db=0)

    # prepare filename
    date_today = datetime.today()
    if date_string is None:
        date_today_string  = date_today.strftime('%d%m%y')
    else:
        date_today_string = date_string
    filename = 'EQ'+date_today_string+'_CSV.ZIP'
    filename_inside_zip = 'EQ'+date_today_string+'.CSV'

    # prepare request body
    headers = settings.BSE_EQUITY_BHAVCOPY_VALID_HEADER
    url = settings.BSE_EQUITY_BHAVCOPY_ENDPOINT+filename
    

    # send request
    response = requests.get(url, headers=headers)

    # unzip
    zip_stream = BytesIO(response.content)
    zip_file = ZipFile(zip_stream)
    zip_file.extract(filename_inside_zip)


    with open(filename_inside_zip, newline='') as csvfile:
        all_sc = csv.DictReader(csvfile)
        # load to redis
        for stock in all_sc:
            key = stock['SC_NAME']
            key = key.strip().replace(' ','')
            keys = re.findall('[0-9a-zA-Z]*', key)
            key = ''.join(keys)
        
            redis_instance.hset(key,date_today_string,json.dumps(stock))
            redis_instance.sadd(settings.STOCK_SET_KEY, stock['SC_NAME'].strip())

    os.remove(filename_inside_zip)
