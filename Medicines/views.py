from django.shortcuts import render
from .forms import *
from Core.views import ONViewMixin
from django.views.generic import *


# Create your views here.
class MedicineCreate(ONViewMixin, CreateView):
    title = 'إضافة دواء'
    model = Medicine
    template_name = 'forms/form_template.html'
    form_class = MedicineForm


class MedicineList(ONViewMixin, ListView):
    title = 'عرض الأدوية'
    model = Medicine
    queryset = Medicine.objects.filter(deleted=False)
    form_class = MedicineForm


class MedicineTrashList(ONViewMixin, ListView):
    title = 'عرض الأدوية المحذوفة'
    model = Medicine
    queryset = Medicine.objects.filter(deleted=True)


class MedicineUpdate(ONViewMixin, UpdateView):
    title = 'تعديل الدواء'
    model = Medicine
    template_name = 'forms/form_template.html'
    form_class = MedicineForm


class MedicineDelete(ONViewMixin, UpdateView):
    title = 'حذف الدواء'
    model = Medicine
    template_name = 'forms/form_template.html'
    form_class = MedicineDeleteForm
