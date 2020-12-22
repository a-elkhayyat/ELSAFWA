from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin
from .forms import *
from Core.views import ONViewMixin
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination


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
    last_entry = patient.heightandweight_set.last()
    if last_entry:
        form.fields['height'].initial = last_entry.height
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
        form.save_m2m()
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
        form.save_m2m()
        return redirect('Patients:PatientDetail', patient.id)
    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'forms/form_template.html', context)


def lab_test_request(request, pk):
    patient = get_object_or_404(Patient, id=pk)
    title = 'طلب تحليل'
    form = LabTestRequestForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.patient = patient
        obj.save()
        return redirect('Patients:PatientDetail', patient.id)
    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'forms/form_template.html', context)


def add_lab_test_result(request, pk):
    lab_test = get_object_or_404(LabTestRequest, id=pk)
    title = 'إدخال نتيجة التحاليل'
    for x in lab_test.lab_test.labtestattribute_set.all():
        result = LabTestResult()
        result.lab_test = lab_test
        result.attribute = x
        result.save()
    return redirect('Patients:LabTestRequestDetail', lab_test.id)


class LabTestRequestDetail(ONViewMixin, DetailView):
    model = LabTestRequest
    title = 'نتائج التحليل'


class LabTestResultDetail(ONViewMixin, DetailView):
    model = LabTestResult
    title = 'نتائج التحليل'


class LabTestResultUpdate(ONViewMixin, UpdateView):
    model = LabTestResult
    title = 'تعديل نتائج التحليل'
    template_name = 'forms/form_template.html'
    form_class = LabTestResultForm


def radiology_request(request, pk):
    patient = get_object_or_404(Patient, id=pk)
    title = 'طلب آشعة'
    form = RadiologyRequestForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.patient = patient
        obj.save()
        return redirect('Patients:PatientDetail', patient.id)
    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'forms/form_template.html', context)


def add_radiology_result(request, pk):
    radiology = get_object_or_404(RadiologyRequest, id=pk)
    title = 'إدخال نتيجة آشعة'
    form = RadiologyResultForm(request.POST or None)
    if form.is_valid():
        result = form.save(commit=False)
        result.radiology = radiology
        result.save()
        return redirect('Patients:PatientDetail', radiology.patient.id)
    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'forms/form_template.html', context)


class RadiologyResult(ONViewMixin, DetailView):
    title = 'عرض نتائج الاشعة'
    model = RadiologyResult


class PatientViewSet(ModelViewSet):
    queryset = Patient.objects.filter(deleted=False)
    serializer_class = PatientSerializer

    def get_queryset(self):
        queryset = self.queryset.filter(instance=self.request.user.instance)
        if self.request.GET.get('q'):
            queryset = queryset.filter(Q(name__icontains=self.request.GET.get('q')) | Q(
                telephone__icontains=self.request.GET.get('q')))
        return queryset


def add_session(request, pk):
    patient = get_object_or_404(Patient, id=pk)
    form = SessionForm(request.POST or None)
    title = 'إضافة جلسة'
    if form.is_valid():
        s = form.save(commit=False)
        s.patient = patient
        s.added_by = request.user
        s.save()
        redirect(request.POST.get('url'))
    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'forms/form_template.html', context)


class SessionUpdate(ONViewMixin, UpdateView):
    title = 'تعديل جلسة'
    model = Session
    form_class = SessionForm
    template_name = 'forms/form_template.html'


class DiagnosisList(ONViewMixin, ListView):
    title = 'عرض التشخيصات'
    model = Diagnosis


class DiagnosisCreate(ONViewMixin, CreateView):
    title = 'إضافة تشخيص'
    model = Diagnosis
    form_class = DiagnosisForm
    template_name = 'forms/form_template.html'


class DiagnosisUpdate(ONViewMixin, UpdateView):
    title = 'تعديل تشخيص'
    model = Diagnosis
    form_class = DiagnosisForm
    template_name = 'forms/form_template.html'


class DiseaseList(ONViewMixin, ListView):
    title = 'عرض التشخيصات'
    model = Disease


class DiseaseCreate(ONViewMixin, CreateView):
    title = 'إضافة تشخيص'
    model = Disease
    form_class = DiseaseForm
    template_name = 'forms/form_template.html'


class DiseaseUpdate(ONViewMixin, UpdateView):
    title = 'تعديل تشخيص'
    model = Disease
    form_class = DiseaseForm
    template_name = 'forms/form_template.html'
