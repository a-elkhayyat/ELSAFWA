from django.urls import path
from .views import *


app_name = 'Invoices'
urlpatterns = [
    path('pay/<int:pk>/', pay, name='Pay'),
    path('patient/sales/<int:pk>/', add_product_invoice, name='add_product_invoice'),
    path('outcome/create/', create_outcome_invoice, name='create_outcome_invoice'),
    path('outcome/list/', OutcomeInvoiceList.as_view(), name='OutcomeInvoiceList'),
    path('outcome/update/<int:pk>/', OutcomeUpdate.as_view(), name='OutcomeUpdate'),
    path('income/list/', IncomeInvoiceList.as_view(), name='IncomeInvoiceList'),
    path('income/update/<int:pk>/', IncomeUpdate.as_view(), name='IncomeUpdate'),
    path('categories/list/', CategoryList.as_view(), name='CategoryList'),
    path('categories/trash/', CategoryTrash.as_view(), name='CategoryTrash'),
    path('categories/create/', CategoryCreate.as_view(), name='CategoryCreate'),
    path('categories/update/<int:pk>/', CategoryUpdate.as_view(), name='CategoryUpdate'),
    path('categories/delete/<int:pk>/', CategoryDelete.as_view(), name='CategoryDelete'),
]