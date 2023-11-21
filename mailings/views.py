from django.forms import SplitDateTimeField
from django.forms.widgets import SplitDateTimeWidget
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Mailing, Client, Periods, MailingLog, Audience
from users.permissions_mixins import ManagerRequiredMixin

DATETIME_WIDGET = SplitDateTimeWidget(date_attrs={'type': 'date', 'class': 'my-2'}, time_attrs={'type': 'time'})


class MailingListView(ManagerRequiredMixin, ListView):
    model = Mailing

    extra_context = {
        'title': 'Рассылки',
        'nbar': 'mailings',
    }


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

    extra_context = {
        'title': 'Клиенты',
        'nbar': 'clients'
    }


class PeriodsCreateView(CreateView):
    model = Periods
    fields = ('name', 'duration')
    success_url = reverse_lazy('mailings:periods_list')


class PeriodsListView(ListView):
    model = Periods

    extra_context = {
        'title': 'Периоды',
        'nbar': 'periods',
    }


class MailingLogListView(ListView):
    model = MailingLog

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)

        context_data['mailings'] = Mailing.objects.all()
        context_data['title'] = 'Логи'
        context_data['nbar'] = 'logs'
        context_data['selected_mailing_pk'] = int(self.request.POST.get('mailing', 0))

        return context_data

    def get_queryset(self):
        mailing_pk = self.request.POST.get('mailing', 0)

        mailing_pk_list = list(Mailing.objects.values_list('pk', flat=True))

        if int(mailing_pk) in mailing_pk_list:
            return self.model.objects.filter(mailing_id=mailing_pk)
        return self.model.objects.all()

    def post(self, request):
        return self.get(request)


class AudienceListView(ListView):
    model = Audience

    extra_context = {
        'title': "Аудитории",
        'nbar': 'audiences',
    }


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
