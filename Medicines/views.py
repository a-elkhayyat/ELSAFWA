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


class DoseCreate(ONViewMixin, CreateView):
    title = 'إضافة جرعة'
    model = Dose
    template_name = 'forms/form_template.html'
    form_class = DoseForm


class DoseList(ONViewMixin, ListView):
    title = 'عرض الجرعات'
    model = Dose
    queryset = Dose.objects.all()
    form_class = DoseForm


class DoseUpdate(ONViewMixin, UpdateView):
    title = 'تعديل الجرعات'
    model = Dose
    template_name = 'forms/form_template.html'
    form_class = DoseForm


class TimingCreate(ONViewMixin, CreateView):
    title = 'إضافة توقيت دواء'
    model = Timing
    template_name = 'forms/form_template.html'
    form_class = TimingForm


class TimingList(ONViewMixin, ListView):
    title = 'عرض توقيتات الأدوية'
    model = Timing
    queryset = Timing.objects.all()
    form_class = TimingForm


class TimingUpdate(ONViewMixin, UpdateView):
    title = 'تعديل توقيت دواء'
    model = Timing
    template_name = 'forms/form_template.html'
    form_class = TimingForm
