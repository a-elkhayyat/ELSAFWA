from django.shortcuts import render, redirect, get_object_or_404
from Core.views import ONViewMixin
from django.views.generic import *
from .forms import *
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination


# Create your views here.
class ProductList(ONViewMixin, ListView):
    model = Product
    paginate_by = 20
    title = 'عرض المنتجات'

    def get_queryset(self):
        return self.model.objects.filter(deleted=False)


class ProductTrashList(ONViewMixin, ListView):
    model = Product
    paginate_by = 20
    title = 'عرض المنتجات المحذوفة'

    def get_queryset(self):
        return self.model.objects.filter(deleted=True)


class ProductCreate(ONViewMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'forms/form_template.html'
    title = 'إضافة منتج'


class ProductUpdate(ONViewMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'forms/form_template.html'
    title = 'تعديل منتج'


class ProductDelete(ONViewMixin, UpdateView):
    model = Product
    form_class = ProductDeleteForm
    template_name = 'forms/form_template.html'
    title = 'حذف منتج'


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.filter(deleted=False)
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = self.queryset.filter(instance=self.request.user.instance)
        if self.request.GET.get('q'):
            queryset = queryset.filter(Q(name__icontains=self.request.GET.get('q')))
        return queryset
