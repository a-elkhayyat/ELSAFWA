from django.urls import path
from .views import *


app_name = 'Invoices'
urlpatterns = [
    path('pay/', pay, name='Pay'),
]