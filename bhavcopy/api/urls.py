from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = {
    path('key', views.set_key, name='keys'),
    path('stocks/details', views.get_details_of_stock_by_date),
    path('stocks', views.get_stocks)
}

urlpatterns = format_suffix_patterns(urlpatterns)