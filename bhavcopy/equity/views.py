from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests
from .tasks import download_equity_bhavcopy_zip
from django.conf import settings

# Create your views here.
def index(request):
    return render(request, 'equity/index.html')

def get_equity_details(request, date):
    print(settings.STATICFILES_DIRS)
    download_equity_bhavcopy_zip(date)   
    return HttpResponse('download complete')


