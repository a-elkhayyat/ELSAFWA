from django.shortcuts import render
from django.views.generic import *
from Core.views import ONViewMixin
from .forms import *


# Create your views here.
class ServiceList(ONViewMixin, ListView):
    title = 'عرض الخدمات'
    model = Service


class ServiceCreate(ONViewMixin, CreateView):
    title = 'إضافة خدمة'
    model = Service
    form_class = ServiceForm
    template_name = 'forms/form_template.html'


class ServiceUpdate(ONViewMixin, UpdateView):
    title = 'تعديل خدمة'
    model = Service
    form_class = ServiceForm
    template_name = 'forms/form_template.html'

