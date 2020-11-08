from .views import *
from django.urls import path

app_name = 'Calendar'
urlpatterns = [
    path('', CalendarList.as_view(), name='CalendarList'),
    ]
