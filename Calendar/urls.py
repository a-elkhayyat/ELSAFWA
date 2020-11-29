from .views import *
from django.urls import path
from rest_framework import routers

app_name = 'Calendar'
router = routers.DefaultRouter()
router.register('calendar', AppointmentViewSet)
urlpatterns = router.urls
urlpatterns += [
    path('list/', CalendarList.as_view(), name='CalendarList'),
    path('today/', today_calendar, name='TodayCalendar'),
    path('create/', AppointmentCreate.as_view(), name='AppointmentCreate'),
    path('update/<int:pk>/', AppointmentUpdate.as_view(), name='AppointmentUpdate'),
    path('queue/attend/<int:pk>/', attend, name='Attend'),
    path('queue/delete/<int:pk>/', delete_queue, name='QueueDelete'),
    path('queue/done/<int:pk>/', done, name='QueueDone'),
    ]
