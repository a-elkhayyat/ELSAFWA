from django.urls import path
from .views import *


app_name = 'Products'

urlpatterns = [
    path('list/', ProductList.as_view(), name='ProductList'),
    path('trash/', ProductTrashList.as_view(), name='ProductTrashList'),
    path('create/', ProductCreate.as_view(), name='ProductCreate'),
    path('update/<int:pk>/', ProductUpdate.as_view(), name='ProductUpdate'),
    path('delete/<int:pk>/', ProductDelete.as_view(), name='ProductDelete'),
]