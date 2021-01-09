from .views import *
from django.urls import path

app_name = 'Core'
urlpatterns = [
    path('', index, name='index'),
    path('users/login/', UserLogin.as_view(), name='UserLogin'),
    path('users/logout/', UserLogout.as_view(), name='UserLogout'),
    path('users/register/', RegisterUser.as_view(), name='RegisterUser'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('permissions/<int:pk>/', permissions, name='permissions'),
    path('login/as/<int:pk>/', login_as, name='login_as'),
    path('password/', change_password, name='change_password'),
    path('users/<int:pk>/reset_password/', PasswordReset.as_view(), name='PasswordReset'),
    path('users/list/', UserList.as_view(), name='UserList'),
    path('users/add/', UserCreate.as_view(), name='UserCreate'),
    path('users/update/<pk>/', UserUpdate.as_view(), name='UserUpdate'),
    path('users/enable/<pk>/', UserDisable.as_view(), name='UserDisable'),
    path('region/country/list/', CountryList.as_view(), name='CountryList'),
    path('region/country/create/', CountryCreate.as_view(), name='CountryCreate'),
    path('region/country/update/<int:pk>/', CountryUpdate.as_view(), name='CountryUpdate'),
    path('region/state/list/', StateList.as_view(), name='StateList'),
    path('region/state/create/', StateCreate.as_view(), name='StateCreate'),
    path('region/state/update/<int:pk>/', StateUpdate.as_view(), name='StateUpdate'),
    path('region/city/list/', CityList.as_view(), name='CityList'),
    path('region/city/create/', CityCreate.as_view(), name='CityCreate'),
    path('region/city/update/<int:pk>/', CityUpdate.as_view(), name='CityUpdate'),
    path('region/area/list/', AreaList.as_view(), name='AreaList'),
    path('region/area/create/', AreaCreate.as_view(), name='AreaCreate'),
    path('region/area/update/<int:pk>/', AreaUpdate.as_view(), name='AreaUpdate'),
]