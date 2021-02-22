from django.shortcuts import render
from Core.views import ONViewMixin
from django.views.generic import *
from django.db.models import Sum
from .forms import *


# Create your views here.
def invoices_report(request):
    form = FromToForm(request.POST or None)
    title = 'تقارير الخزينة'
    context = {
        'form': form,
        'title': title,
    }
    if form.is_valid():
        object_list = Invoice.objects.filter(added_at__date__gte=form.cleaned_data['from_date'],
                                             added_at__date__lte=form.cleaned_data['to_date'],
                                             instance=request.user.instance)
        income = object_list.filter(invoice_type=1).aggregate(total=Sum('paid'))
        outcome = object_list.filter(invoice_type=2).aggregate(total=Sum('outcome'))
        sales_invoices = object_list.filter(invoice_type=1).filter(is_invoice=True).aggregate(total=Sum('paid'))
        services_invoices = object_list.filter(invoice_type=1).filter(is_invoice=False).aggregate(total=Sum('paid'))
        context.update({
            'object_list': object_list,
            'income': income,
            'outcome': outcome,
            'sales_invoices': sales_invoices,
            'services_invoices': services_invoices,
        })
    return render(request, 'Reports/invoices_reports.html', context)


def category_reports(request):
    form = FromToForm(request.POST or None)
    title = 'تقارير الدخل'
    context = {
        'form': form,
        'title': title,
    }
    if form.is_valid():
        object_list = Invoice.objects.filter(added_at__date__gte=form.cleaned_data['from_date'],
                                             added_at__date__lte=form.cleaned_data['to_date'],
                                             instance=request.user.instance)
        sales = object_list.exclude(product__isnull=True).order_by('product')
        sales_total = sales.aggregate(total=Sum('after_discount'), paid=Sum('paid'))
        sales_total_by_product = sales.values('product__name').annotate(sum=Sum('after_discount'))
        services = object_list.exclude(service__isnull=True).order_by('service')
        services_total = services.aggregate(total=Sum('after_discount'), paid=Sum('paid'))
        services_total_by_service = services.values('service__name').annotate(sum=Sum('after_discount'))
        context.update({
            'object_list': object_list,
            'sales': sales,
            'services': services,
            'sales_total': sales_total,
            'services_total': services_total,
            'sales_total_by_product': sales_total_by_product,
            'services_total_by_service': services_total_by_service,
        })
    return render(request, 'Reports/category_reports.html', context)
