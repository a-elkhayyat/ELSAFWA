from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import *
from Core.views import ONViewMixin
from rest_framework.viewsets import ModelViewSet
from .forms import *
from .serializers import *


# Create your views here.
class LabTestCreate(ONViewMixin, CreateView):
    title = 'إضافة تحليل'
    model = LabTest
    form_class = LabTestForm
    template_name = 'forms/form_template.html'
    success_url = reverse_lazy('LabTest:LabTestList')


class LabTestList(ONViewMixin, ListView):
    title = 'عرض التحاليل'
    model = LabTest
    paginate_by = 20


class LabTestUpdate(ONViewMixin, UpdateView):
    title = 'تعديل تحليل'
    model = LabTest
    form_class = LabTestForm
    template_name = 'forms/form_template.html'
    success_url = reverse_lazy('LabTest:LabTestList')


class LabTestDelete(ONViewMixin, UpdateView):
    title = 'حذف تحليل'
    model = LabTest
    form_class = LabTestDeleteForm
    template_name = 'forms/form_template.html'
    success_url = reverse_lazy('LabTest:LabTestList')


class LabTestDetail(ONViewMixin, DetailView):
    title = 'عرض التحاليل'
    model = LabTest


def add_lab_test_attribute(request, pk):
    title = 'إضافة خصائص تحليل'
    lab_test = get_object_or_404(LabTest, id=pk)
    form = LabTestAttributeForm(request.POST or None)
    if form.is_valid():
        record = form.save(commit=False)
        record.lab_test = lab_test
        record.save()
        return redirect('LabTest:LabTestDetail', lab_test.id)
    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'forms/form_template.html', context)


class LabTestViewSet(ModelViewSet):
    queryset = LabTest.objects.filter(deleted=False)
    serializer_class = LabTestSerializer
