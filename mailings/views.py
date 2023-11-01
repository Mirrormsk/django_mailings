from django.forms import SplitDateTimeField
from django.forms.widgets import SplitDateTimeWidget
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Mailing, Client, Periods, MailingLog

DATETIME_WIDGET = SplitDateTimeWidget(date_attrs={'type': 'date'}, time_attrs={'type': 'time'})


class MailingListView(ListView):
    model = Mailing


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailings:mailings_list')


class MailingCreateView(CreateView):
    model = Mailing
    fields = ('name', 'period', 'audience', 'start_time', 'end_time', 'message_title', 'message_body')
    success_url = reverse_lazy('mailings:mailings_list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['start_time'] = SplitDateTimeField(widget=DATETIME_WIDGET, label='Время начала')
        form.fields['end_time'] = SplitDateTimeField(widget=DATETIME_WIDGET, label='Время завершения')
        return form


class MailingUpdateView(UpdateView):
    model = Mailing
    fields = ('name', 'period', 'audience', 'start_time', 'end_time', 'message_title', 'message_body')
    success_url = reverse_lazy('mailings:mailings_list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['start_time'] = SplitDateTimeField(widget=DATETIME_WIDGET, label='Время начала')
        form.fields['end_time'] = SplitDateTimeField(widget=DATETIME_WIDGET, label='Время начала')
        return form


class ClientCreateView(CreateView):
    model = Client
    fields = ('first_name', 'last_name', 'email', 'note')
    success_url = reverse_lazy('mailings:mailings_list')


class ClientListView(ListView):
    model = Client


class RecipientListView(ListView):
    model = Client


class PeriodsCreateView(CreateView):
    model = Periods
    fields = ('name', 'duration')
    success_url = reverse_lazy('mailings:periods_list')


class PeriodsListView(ListView):
    model = Periods


class MailingLogListView(ListView):
    model = MailingLog


def stop_mailing(request, pk):
    mailing = Mailing.objects.get(pk=pk)
    mailing.status = Mailing.STATUS_FINISHED
    mailing.save()
    return redirect(reverse_lazy('mailings:mailings_list'))


def start_mailing(request, pk):
    mailing = Mailing.objects.get(pk=pk)
    mailing.status = Mailing.STATUS_CREATED
    mailing.save()
    return redirect(reverse_lazy('mailings:mailings_list'))
