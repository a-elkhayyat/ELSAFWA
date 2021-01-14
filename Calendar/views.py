from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import *
from .forms import *
from Core.views import ONViewMixin
from rest_framework.viewsets import ModelViewSet
from .serializers import AppointmentSerializer
from django.db.models import Q


# Create your views here.
class CalendarList(ONViewMixin, ListView):
    model = Appointment
    title = 'الأجندة'
    template_name = 'Calendar/calendar_list.html'

    def get_queryset(self):
        queryset = Appointment.objects.filter(instance=self.request.user.instance)
        if self.request.GET.get('start'):
            queryset = queryset.filter(date__date__gte=self.request.GET.get('start'))
        else:
            queryset = queryset.filter(date__date__month=now().date().month)
        if self.request.GET.get('end'):
            queryset = queryset.filter(date__date__lte=self.request.GET.get('end'))
        else:
            queryset = queryset.filter(date__date__month=now().date().month)
        return queryset


class AppointmentCreate(ONViewMixin, CreateView):
    model = Appointment
    title = 'إنشاء موعد'
    template_name = 'Calendar/add_appointment_form.html'
    form_class = AppointmentForm
    success_url = reverse_lazy('Calendar:CalendarList')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['n'] = self.request.user.instance
        return kwargs


class AppointmentUpdate(ONViewMixin, UpdateView):
    model = Appointment
    title = 'تعديل موعد'
    template_name = 'Calendar/add_appointment_form.html'
    form_class = AppointmentForm
    success_url = reverse_lazy('Calendar:CalendarList')

    def get_form_kwargs(self):
        kwargs = super(AppointmentUpdate, self).get_form_kwargs()
        kwargs['n'] = self.request.user.instance
        return kwargs


def today_calendar(request):
    title = 'مواعيد اليوم'
    appointments = Appointment.objects.filter(instance=request.user.instance, date__date=now().today())
    queues = Queue.objects.filter(instance=request.user.instance, done=False)

    context = {
        'appointments': appointments,
        'queues': queues,
        'title': title
    }
    return render(request, 'Calendar/today_calendar.html', context)


class AppointmentViewSet(ModelViewSet):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()

    def get_queryset(self):
        queryset = self.queryset.filter(instance=self.request.user.instance)
        if self.request.GET.get('q'):
            queryset = queryset.filter(Q(start__gte=self.request.GET.get('start')) | Q(
                date__lte=self.request.GET.get('end')))
        return queryset


def attend(request, pk):
    appointment = get_object_or_404(Appointment, id=pk)
    if appointment.queue_set.count() > 0:
        return redirect('Calendar:TodayCalendar')
    queue = Queue()
    queue.appointment = appointment
    queue.service = appointment.service
    queue.instance = request.user.instance
    queue.patient = appointment.patient
    queue.save()
    return redirect('Calendar:TodayCalendar')


def delete_queue(request, pk):
    queue = get_object_or_404(Queue, id=pk)
    queue.delete()
    return redirect('Calendar:TodayCalendar')


def done(request, pk):
    queue = get_object_or_404(Queue, id=pk)
    queue.done = True
    queue.save()
    return redirect('Calendar:TodayCalendar')
