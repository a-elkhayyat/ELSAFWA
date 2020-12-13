from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import *
from .forms import *
from Core.views import ONViewMixin


# Create your views here.
class DeviceList(ONViewMixin, ListView):
    title = 'عرض الأجهزة'
    model = Device
    paginate_by = 20
    
    
class DeviceCreate(ONViewMixin, CreateView):
    title = 'إضافة جهاز'
    model = Device
    template_name = 'forms/form_template.html'
    form_class = DeviceForm
    

class DeviceUpdate(ONViewMixin, UpdateView):
    title = 'تعديل جهاز'
    model = Device
    template_name = 'forms/form_template.html'
    form_class = DeviceForm


class ExerciseList(ONViewMixin, ListView):
    title = 'عرض التمرينات'
    model = Exercise
    paginate_by = 20


class ExerciseCreate(ONViewMixin, CreateView):
    title = 'إضافة تمرين'
    model = Exercise
    template_name = 'forms/form_template.html'
    form_class = ExerciseForm


class ExerciseUpdate(ONViewMixin, UpdateView):
    title = 'تعديل تمرين'
    model = Exercise
    template_name = 'forms/form_template.html'
    form_class = ExerciseForm

