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
    path('diet/add/<int:pk>/', add_diet, name='add_diet'),
    path('diet/update/<int:pk>/', DietUpdate.as_view(), name='DietUpdate'),
    path('prescription/add/<int:pk>/', add_prescription, name='add_prescription'),
    path('prescription/<int:pk>/detail/', view_prescription, name='view_prescription'),
    path('prescription/item/<int:pk>/update/', PrescriptionItemUpdate.as_view(), name='PrescriptionItemUpdate'),
    path('prescription/item/<int:pk>/delete/', prescription_item_delete, name='prescription_item_delete'),
    path('record/investigation/<int:pk>/', add_investigation, name='add_investigation'),
    path('record/investigation/<int:pk>/edit', edit_investigation, name='edit_investigation'),
    path('lab_test/request/<int:pk>/', lab_test_request, name='lab_test_request'),
    path('lab_test/add/result/<int:pk>/', add_lab_test_result, name='add_lab_test_result'),
    path('lab_test/result/<int:pk>/', LabTestResultDetail.as_view(), name='LabTestResultDetail'),
    path('lab_test/request/<int:pk>/results/', LabTestRequestDetail.as_view(), name='LabTestRequestDetail'),
    path('lab_test/result/update/<int:pk>/', LabTestResultUpdate.as_view(), name='LabTestResultUpdate'),
    path('radiology/request/<int:pk>/', radiology_request, name='radiology_request'),
    path('radiology/add/result/<int:pk>/', add_radiology_result, name='add_radiology_result'),
    path('radiology/view/result/<int:pk>/', RadiologyResult.as_view(), name='RadiologyResult'),
    path('sessions/create/<int:pk>/', add_session, name='add_session'),
    path('sessions/update/<int:pk>/', SessionUpdate.as_view(), name='SessionUpdate'),
    path('diagnosis/list/', DiagnosisList.as_view(), name='DiagnosisList'),
    path('diagnosis/create/', DiagnosisCreate.as_view(), name='DiagnosisCreate'),
    path('diagnosis/update/<int:pk>/', DiagnosisUpdate.as_view(), name='DiagnosisUpdate'),
    path('disease/list/', DiseaseList.as_view(), name='DiseaseList'),
    path('disease/create/', DiseaseCreate.as_view(), name='DiseaseCreate'),
    path('disease/update/<int:pk>/', DiseaseUpdate.as_view(), name='DiseaseUpdate'),
    path('images/add/<int:pk>/', add_image, name='add_image'),
    path('images/delete/<int:pk>/', delete_image, name='delete_image'),
    path('images/view/<int:pk>/', add_image, name='add_image'),
]
