from django.urls import path
from .views import *


app_name = 'Medicines'
urlpatterns = [
    path('list/', MedicineList.as_view(), name='MedicineList'),
    path('trash/', MedicineTrashList.as_view(), name='MedicineTrashList'),
    path('create/', MedicineCreate.as_view(), name='MedicineCreate'),
    path('<int:pk>/update/', MedicineUpdate.as_view(), name='MedicineUpdate'),
    path('<int:pk>/delete/', MedicineDelete.as_view(), name='MedicineDelete'),
    path('dose/list/', DoseList.as_view(), name='DoseList'),
    path('dose/create/', DoseCreate.as_view(), name='DoseCreate'),
    path('dose/<int:pk>/update/', DoseUpdate.as_view(), name='DoseUpdate'),
    path('timing/list/', TimingList.as_view(), name='TimingList'),
    path('timing/create/', TimingCreate.as_view(), name='TimingCreate'),
    path('timing/<int:pk>/update/', TimingUpdate.as_view(), name='TimingUpdate'),
]
