from django.urls import path
from .views import *


app_name = 'PhysicalTherapy'
urlpatterns = [
    path('devices/list/', DeviceList.as_view(), name='DeviceList'),
    path('devices/create/', DeviceCreate.as_view(), name='DeviceCreate'),
    path('devices/update/<int:pk>/', DeviceUpdate.as_view(), name='DeviceUpdate'),
    path('exercises/list/', ExerciseList.as_view(), name='ExerciseList'),
    path('exercises/create/', ExerciseCreate.as_view(), name='ExerciseCreate'),
    path('exercises/update/<int:pk>/', ExerciseUpdate.as_view(), name='ExerciseUpdate'),
]