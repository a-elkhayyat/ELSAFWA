from django.urls import path
from .views import *


app_name = 'Medicines'
urlpatterns = [
    path('list/', MedicineList.as_view(), name='MedicineList'),
    path('trash/', MedicineTrashList.as_view(), name='MedicineTrashList'),
    path('create/', MedicineCreate.as_view(), name='MedicineCreate'),
    path('<int:pk>/update/', MedicineUpdate.as_view(), name='MedicineUpdate'),
    path('<int:pk>/delete/', MedicineDelete.as_view(), name='MedicineDelete'),
]
