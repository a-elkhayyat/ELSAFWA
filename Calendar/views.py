from django.shortcuts import render
from django.views.generic import *
from .models import *
from Core.views import ONViewMixin


# Create your views here.
class CalendarList(ONViewMixin, ListView):
    model = Appointment
    title = 'الأجندة'
