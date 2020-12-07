from django.shortcuts import render
from django.views.generic import *
from Core.views import ONViewMixin
from .forms import *


# Create your views here.
class ServiceList(ONViewMixin, ListView):
    title = 'عرض الخدمات'
    model = Service
    queryset = Service.objects.filter(deleted=False)

    def get_queryset(self):
        return self.queryset.filter(instance=self.request.user.instance)


class ServiceTrashList(ONViewMixin, ListView):
    title = 'عرض الخدمات المحذوفة'
    model = Service
    queryset = Service.objects.filter(deleted=True)

    def get_queryset(self):
        return self.queryset.filter(instance=self.request.user.instance)


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


class ServiceDelete(ONViewMixin, UpdateView):
    title = 'حذف خدمة'
    model = Service
    form_class = ServiceDeleteForm
    template_name = 'forms/form_template.html'
