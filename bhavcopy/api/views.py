from django.shortcuts import render
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework  import status
from rest_framework.response import Response
import redis
import json
import re
from .tasks import add
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt


redis_instance = redis.StrictRedis(host = settings.REDIS_HOST, port=settings.REDIS_PORT, password=settings.REDIS_PASSWORD, db=0)

# Create your views here.

@api_view(['GET','POST'])
def get_details_of_stock_by_date(request):
    
    data_requested = request.data
    stock_list = list()
    requested_stock_details = data_requested['data']
    

    for stock in requested_stock_details:
        key = stock['stockName'].strip().replace(' ','')
        keys = re.findall('[0-9a-zA-Z]*', key)
        key = ''.join(keys)
        date_string = datetime.strptime(stock['date'],"%Y-%m-%d").strftime('%d%m%y')
        fetched_data = redis_instance.hget(key,date_string)
        if fetched_data is None:
            continue
        res = json.loads(fetched_data)
        stock_list.append(res)
    
    return Response(stock_list, 200)


@api_view(['GET'])
def get_stocks(request):
    stockList = redis_instance.smembers(settings.STOCK_SET_KEY)
    
    return Response({
        "stockNames":stockList
    }, 200)

@api_view(['POST'])
def set_key(request, *args, **kwargs):
    value = json.loads(request.body)
    value_to_store = {'a':1,'b':2,'c':[3,4,5]}
    # keys = list(value.keys())
    # print(keys)
    key = 'ABB LTD.'
    key = key.strip().replace(' ','')
    keys = re.findall('[0-9a-zA-Z]*', key)
    key = ''.join(keys)
    date ='070521'
    redis_instance.hset(key, date, json.dumps(value_to_store))
    return Response(f'key successfully inserted {key}', 201)

