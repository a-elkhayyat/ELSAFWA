from django.shortcuts import render, redirect, get_object_or_404
from Patients.models import Patient
from Services.models import Service
from Core.models import Instance, User
from Calendar.models import Queue
from .forms import *


# Create your views here.
def pay(request, pk):
    title = 'دفع'
    queue = get_object_or_404(Queue, id=pk)
    form = InvoiceForm(request.POST or None)
    if form.is_valid():
        invoice = InvoiceForm.save(commit=False)
        invoice.patient = queue.patient
        invoice.service = queue.service
        invoice.visits_added = queue.service.number_of_visits
        invoice.visits_used = 1
        invoice.save()
        return redirect('Calendar:TodayCalendar')
    context = {
        'title': title,
        'queue': queue,
        'form': form,
    }
    return render(request, 'forms/form_template.html', context)

