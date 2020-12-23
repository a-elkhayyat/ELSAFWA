from django.shortcuts import render
from Core.views import ONViewMixin
from django.views.generic import *
from .forms import *


# Create your views here.
class DietList(ONViewMixin, ListView):
    model = Diet
    title = 'عرض الأنظمة الغذائية'

    def get_queryset(self):
        return self.model.objects.filter(deleted=False)


class DietTrashList(ONViewMixin, ListView):
    model = Diet
    title = ' عرض الأنظمة الغذائية المحذوفة'

    def get_queryset(self):
        return self.model.objects.filter(deleted=True)


class DietCreate(ONViewMixin, CreateView):
    model = Diet
    form_class = DietForm
    template_name = 'forms/form_template.html'
    title = 'إضافة نظام غذائي'


class DietUpdate(ONViewMixin, UpdateView):
    model = Diet
    form_class = DietForm
    template_name = 'forms/form_template.html'
    title = 'تعديل نظام غذائي'


class DietDelete(ONViewMixin, UpdateView):
    model = Diet
    form_class = DietDeleteForm
    template_name = 'forms/form_template.html'
    title = 'حذف نظام غذائي'

