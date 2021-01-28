from django.urls import path
from .views import *
from rest_framework import routers


app_name = 'Diet'

router = routers.DefaultRouter()
router.register('diet', ProductViewSet)
urlpatterns = router.urls
urlpatterns += [
    path('list/', DietList.as_view(), name='DietList'),
    path('trash/', DietTrashList.as_view(), name='DietTrashList'),
    path('create/', DietCreate.as_view(), name='DietCreate'),
    path('update/<int:pk>/', DietUpdate.as_view(), name='DietUpdate'),
    path('delete/<int:pk>/', DietDelete.as_view(), name='DietDelete'),
]