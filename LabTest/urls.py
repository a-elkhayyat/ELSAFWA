from django.urls import path
from .views import *
from rest_framework import routers


app_name = 'LabTest'
router = routers.DefaultRouter()
router.register('lab_test', LabTestViewSet)
urlpatterns = router.urls
urlpatterns += [
    path('create/', LabTestCreate.as_view(), name='LabTestCreate'),
    path('list/', LabTestList.as_view(), name='LabTestList'),
    path('update/<int:pk>/', LabTestUpdate.as_view(), name='LabTestUpdate'),
    path('detail/<int:pk>/', LabTestDetail.as_view(), name='LabTestDetail'),
    path('delete/<int:pk>/', LabTestDelete.as_view(), name='LabTestDelete'),
    path('add/attribute/<int:pk>', add_lab_test_attribute, name='add_lab_test_attribute')
]