from django.shortcuts import render, redirect, get_object_or_404
from Patients.models import Patient
from Services.models import Service
from Core.models import Instance, User
from django.views.generic import *
from Core.views import ONViewMixin
from Calendar.models import Queue
from .forms import *


# Create your views here.
def pay(request, pk):
    title = 'دفع'
    queue = get_object_or_404(Queue, id=pk)
    patient = queue.patient
    invoices = patient.invoice_set.all()
    form = InvoiceForm(request.POST or None)
    form.fields['price'].initial = queue.service.price
    form.fields['after_discount'].initial = queue.service.price
    form.fields['price'].readonly = True
    form.fields['after_discount'].readonly = True
    form.fields['old_balance'].initial = patient.balance()
    form.fields['remaining'].initial = 0
    if form.is_valid():
        invoice = form.save(commit=False)
        invoice.patient = queue.patient
        invoice.service = queue.service
        invoice.visits_added = queue.service.number_of_visits
        invoice.visits_used = 1
        invoice.invoice_type = 1
        invoice.save()
        queue = Queue()
        queue.service = invoice.service
        queue.patient = invoice.patient
        queue.instance = request.user.instance
        queue.count = invoice.visits_added
        queue.done = True
        queue.save()
        return redirect('Calendar:TodayCalendar')
    context = {
        'title': title,
        'queue': queue,
        'form': form,
        'invoices': invoices,
    }
    return render(request, 'Invoices/invoice_form.html', context)


class CategoryList(ONViewMixin, ListView):
    title = 'تصنيفات المصروفات'
    model = OutcomeCategory
    paginate_by = 20

    def get_queryset(self):
        return self.request.user.instance.outcomecategory_set.all().filter(deleted=False)


class CategoryTrash(ONViewMixin, ListView):
    title = 'تصنيفات المصروفات'
    model = OutcomeCategory
    paginate_by = 20

    def get_queryset(self):
        return self.request.user.instance.outcomecategory_set.all().filter(deleted=True)


class CategoryCreate(ONViewMixin, CreateView):
    title = 'إضافة تصنيف مصروفات'
    model = OutcomeCategory
    form_class = CategoryForm
    template_name = 'forms/form_template.html'


class CategoryUpdate(ONViewMixin, UpdateView):
    title = 'تعديل تصنيف مصروفات'
    model = OutcomeCategory
    form_class = CategoryForm
    template_name = 'forms/form_template.html'


class CategoryDelete(ONViewMixin, UpdateView):
    title = 'حذف تصنيف مصروفات'
    model = OutcomeCategory
    form_class = CategoryDeleteForm
    template_name = 'forms/form_template.html'


def create_outcome_invoice(request):
    title = 'سند صرف نقدية'
    form = OutcomeForm(request.POST or None)
    form.fields['category'].queryset = request.user.instance.outcomecategory_set.filter(deleted=False)
    if form.is_valid():
        invoice = form.save(commit=False)
        invoice.added_by = request.user
        invoice.invoice_type = 2
        invoice.save()
        return redirect(request.POST.get('url'))
    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'forms/form_template.html', context)


class OutcomeInvoiceList(ONViewMixin, ListView):
    title = 'عرض سندات الصرف'
    paginate_by = 20
    model = Invoice
    template_name = 'Invoices/outcome_invoices.html'

    def get_queryset(self):
        return Invoice.objects.filter(instance=self.request.user.instance, invoice_type=2)


class IncomeInvoiceList(ONViewMixin, ListView):
    title = 'عرض سندات القبض'
    paginate_by = 20
    model = Invoice
    template_name = 'Invoices/income_invoices.html'

    def get_queryset(self):
        return Invoice.objects.filter(instance=self.request.user.instance, invoice_type=1)


class OutcomeUpdate(ONViewMixin, UpdateView):
    title = 'تعديل سند صرف نقدية'
    model = Invoice
    form_class = OutcomeForm
    template_name = 'forms/form_template.html'


class IncomeUpdate(ONViewMixin, UpdateView):
    title = 'تعديل سند قبض نقدية'
    model = Invoice
    form_class = InvoiceForm
    template_name = 'Invoices/invoice_form.html'


def add_product_invoice(request, pk):
    title = 'بيع منتج'
    patient = get_object_or_404(Patient, id=pk)
    form = ProductInvoiceForm(request.POST or None)
    if form.is_valid():
        invoice = form.save(commit=False)
        invoice.patient = patient
        invoice.added_by = request.user
        invoice.save()
        return redirect(request.POST.get('url'))
    context = {
        'title': title,
        'patient': patient,
        'form': form,
    }
    return render(request, 'Invoices/product_invoice_form.html', context)
