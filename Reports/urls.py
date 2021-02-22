from django.urls import path
from .views import *


app_name = 'Reports'
urlpatterns = [
    path('invoices/', invoices_report, name='invoices_report'),
    path('category/', category_reports, name='category_reports'),
]