from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin
from .forms import *
from Core.views import ONViewMixin
from rest_framework.viewsets import ModelViewSet
from .serializers import *


# Create your views here.
class PatientList(ONViewMixin, ListView):
    model = Patient
    paginate_by = 20
    title = 'عرض المرضي'

    def get_queryset(self):
        queryset = self.model.objects.filter(deleted=False, instance=self.request.user.instance)
        if self.request.GET.get('name'):
            queryset = queryset.filter(name__icontains=self.request.GET.get('name'))
        if self.request.GET.get('telephone'):
            queryset = queryset.filter(telephone__icontains=self.request.GET.get('telephone'))
        if self.request.GET.get('gender'):
            queryset = queryset.filter(gender=self.request.GET.get('gender'))
        return queryset


class PatientTrash(ONViewMixin, ListView):
    model = Patient
    paginate_by = 20
    title = 'عرض المرضي المحذوفين'

    def get_queryset(self):
        queryset = self.model.objects.filter(deleted=True, instance=self.request.user.instance)
        if self.request.GET.get('name'):
            queryset = queryset.filter(name__icontains=self.request.GET.get('name'))
        if self.request.GET.get('telephone'):
            queryset = queryset.filter(telephone__icontains=self.request.GET.get('telephone'))
        if self.request.GET.get('gender'):
            queryset = queryset.filter(gender=self.request.GET.get('gender'))
        return queryset


class PatientCreate(ONViewMixin, CreateView):
    model = Patient
    form_class = PatientForm
    template_name = 'forms/form_template.html'
    title = 'إضافة مريض'
    success_url = reverse_lazy('Patients:PatientList')


class PatientUpdate(ONViewMixin, UpdateView):
    model = Patient
    form_class = PatientForm
    template_name = 'forms/form_template.html'
    title = 'تعديل بيانات مريض'
    success_url = reverse_lazy('Patients:PatientList')


class PatientDelete(ONViewMixin, UpdateView):
    model = Patient
    form_class = PatientDeleteForm
    template_name = 'forms/form_template.html'
    title = 'حذف مريض'
    success_url = reverse_lazy('Patients:PatientList')


class PatientDetail(ONViewMixin, DetailView):
    model = Patient
    title = 'عرض بيانات مريض'


class PatientHistoryUpdate(ONViewMixin, UpdateView):
    model = Patient
    form_class = PatientHistoryForm
    template_name = 'forms/form_template.html'
    title = 'تعديل التاريخ المرضي'
    success_url = reverse_lazy('Patients:PatientList')


def add_vital_record(request, pk):
    patient = get_object_or_404(Patient, id=pk)
    title = 'إضافة سجل العمليات الحيوية'
    form = VitalRecordForm(request.POST or None)
    if form.is_valid():
        record = form.save(commit=False)
        record.patient = patient
        record.save()
        return redirect('Patients:PatientDetail', patient.id)
    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'forms/form_template.html', context)


def add_height_and_weight(request, pk):
    patient = get_object_or_404(Patient, id=pk)
    title = 'إضافة سجل الوزن والطول'
    form = HeightAndWeightForm(request.POST or None)
    if form.is_valid():
        record = form.save(commit=False)
        record.patient = patient
        record.save()
        record.calculate_bmi()
        return redirect('Patients:PatientDetail', patient.id)
    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'forms/form_template.html', context)


def add_investigation(request, pk):
    patient = get_object_or_404(Patient, id=pk)
    title = 'إضافة زيارة كشف'
    form = InvestigationForm(request.POST or None)
    if form.is_valid():
        record = form.save(commit=False)
        record.patient = patient
        record.save()
        return redirect('Patients:PatientDetail', patient.id)
    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'forms/form_template.html', context)


def edit_investigation(request, pk):
    investigation = get_object_or_404(PatientInvestigation, id=pk)
    patient = investigation.patient
    title = 'تعديل زيارة كشف'
    form = InvestigationForm(request.POST or None, instance=investigation)
    if form.is_valid():
        record = form.save(commit=False)
        record.patient = patient
        record.save()
        return redirect('Patients:PatientDetail', patient.id)
    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'forms/form_template.html', context)


class PatientViewSet(ModelViewSet):
    queryset = Patient.objects.filter(deleted=False)
    serializer_class = PatientSerializer

