from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('download/<str:date>', views.get_equity_details, name='equity_zip')
]