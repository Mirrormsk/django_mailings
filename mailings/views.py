from django.contrib.admin.widgets import AdminSplitDateTime
from django.forms.widgets import SplitDateTimeWidget
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from .models import Mailing, Client, Periods, Message


class MailingListView(ListView):
    model = Mailing


class MailingCreateView(CreateView):
    model = Mailing
    fields = ('name', 'period', 'start_time', 'end_time', 'content')
    success_url = reverse_lazy('mailings:mailings_list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['start_time'].widget = AdminSplitDateTime()
        form.fields['end_time'].widget = AdminSplitDateTime()
        return form


class MailingUpdateView(UpdateView):
    model = Mailing
    fields = ('name', 'period', 'start_time', 'end_time', 'content')
    success_url = reverse_lazy('mailings:mailings_list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['start_time'].widget = AdminSplitDateTime()
        form.fields['end_time'].widget = AdminSplitDateTime()
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


class MessageCreateView(CreateView):
    model = Message
    fields = ('title', 'body')
    success_url = reverse_lazy('mailings:messages_list')


class MessageListView(ListView):
    model = Message
