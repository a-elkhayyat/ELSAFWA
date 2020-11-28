from .views import *
from django.urls import path

app_name = 'Calendar'
urlpatterns = [
    path('', CalendarList.as_view(), name='CalendarList'),
    path('create', AppointmentCreate.as_view(), name='AppointmentCreate'),
    path('update/<int:pk>/', AppointmentUpdate.as_view(), name='AppointmentUpdate'),
    ]
