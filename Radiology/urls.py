from django.urls import path
from .views import *
from rest_framework import routers


app_name = 'Radiology'
router = routers.DefaultRouter()
router.register('radiology', RadiologyViewSet)
urlpatterns = router.urls
urlpatterns += [
    path('create/', RadiologyCreate.as_view(), name='RadiologyCreate'),
    path('list/', RadiologyList.as_view(), name='RadiologyList'),
    path('update/<int:pk>/', RadiologyUpdate.as_view(), name='RadiologyUpdate'),
    path('detail/<int:pk>/', RadiologyDetail.as_view(), name='RadiologyDetail'),
    path('delete/<int:pk>/', RadiologyDelete.as_view(), name='RadiologyDelete'),
]