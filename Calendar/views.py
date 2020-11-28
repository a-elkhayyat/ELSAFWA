from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import *
from .forms import *
from Core.views import ONViewMixin


# Create your views here.
class CalendarList(ONViewMixin, ListView):
    model = Appointment
    title = 'الأجندة'
    template_name = 'Calendar/calendar_list.html'


class AppointmentCreate(ONViewMixin, CreateView):
    model = Appointment
    title = 'إنشاء موعد'
    template_name = 'Calendar/add_appointment_form.html'
    form_class = AppointmentForm
    success_url = reverse_lazy('Calendar:CalendarList')


class AppointmentUpdate(ONViewMixin, UpdateView):
    model = Appointment
    title = 'تعديل موعد'
    template_name = 'Calendar/add_appointment_form.html'
    form_class = AppointmentForm

