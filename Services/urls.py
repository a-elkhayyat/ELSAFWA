from django.urls import path
from .views import *

app_name = 'Services'

urlpatterns = [
    path('list/', ServiceList.as_view(), name='ServiceList'),
    path('trash/', ServiceTrashList.as_view(), name='ServiceTrashList'),
    path('add/', ServiceCreate.as_view(), name='ServiceCreate'),
    path('update/<int:pk>/', ServiceUpdate.as_view(), name='ServiceUpdate'),
    path('delete/<int:pk>/', ServiceDelete.as_view(), name='ServiceDelete'),
]