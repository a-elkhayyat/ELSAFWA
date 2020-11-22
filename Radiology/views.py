from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import *
from Core.views import ONViewMixin
from rest_framework.viewsets import ModelViewSet
from .forms import *
from .serializers import *


# Create your views here.
class RadiologyCreate(ONViewMixin, CreateView):
    title = 'إضافة آشعة'
    model = Radiology
    form_class = RadiologyForm
    template_name = 'forms/form_template.html'
    success_url = reverse_lazy('Radiology:RadiologyList')


class RadiologyList(ONViewMixin, ListView):
    title = 'عرض الآشعة'
    model = Radiology
    paginate_by = 20


class RadiologyUpdate(ONViewMixin, UpdateView):
    title = 'تعديل آشعة'
    model = Radiology
    form_class = RadiologyForm
    template_name = 'forms/form_template.html'
    success_url = reverse_lazy('Radiology:RadiologyList')


class RadiologyDelete(ONViewMixin, UpdateView):
    title = 'حذف آشعة'
    model = Radiology
    form_class = RadiologyDeleteForm
    template_name = 'forms/form_template.html'
    success_url = reverse_lazy('Radiology:RadiologyList')


class RadiologyDetail(ONViewMixin, DetailView):
    title = 'عرض الآشعة'
    model = Radiology


class RadiologyViewSet(ModelViewSet):
    queryset = Radiology.objects.filter(deleted=False)
    serializer_class = RadiologySerializer
