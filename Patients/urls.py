from django.urls import path
from .views import *
from rest_framework import routers


app_name = 'Patients'
router = routers.DefaultRouter()
router.register('patients', PatientViewSet)
urlpatterns = router.urls
urlpatterns += [
    path('list/', PatientList.as_view(), name='PatientList'),
    path('trash/', PatientTrash.as_view(), name='PatientTrash'),
    path('create/', PatientCreate.as_view(), name='PatientCreate'),
    path('update/<int:pk>/', PatientUpdate.as_view(), name='PatientUpdate'),
    path('delete/<int:pk>/', PatientDelete.as_view(), name='PatientDelete'),
    path('view/<int:pk>/', PatientDetail.as_view(), name='PatientDetail'),
    path('update/history/<int:pk>/', PatientHistoryUpdate.as_view(), name='PatientHistoryUpdate'),
    path('record/weight/<int:pk>/', add_height_and_weight, name='add_height_and_weight'),
    path('record/vital/<int:pk>/', add_vital_record, name='add_vital_record'),
    path('record/investigation/<int:pk>/', add_investigation, name='add_investigation'),
]
