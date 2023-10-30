from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .models import Mailing, Client, Periods


class MailingListView(ListView):
    model = Mailing


class MailingCreateView(CreateView):
    model = Mailing
    fields = ('name', 'period', 'start_time', 'end_time')
    success_url = reverse_lazy('mailings:mailings_list')


class ClientCreateView(CreateView):
    model = Client
    fields = ('first_name', 'last_name', 'email', 'note')
    success_url = reverse_lazy('mailings:mailings_list')


class ClientListView(ListView):
    model = Client


class PeriodsCreateView(CreateView):
    model = Periods
    fields = ('name', 'pattern')
    success_url = reverse_lazy('mailings:periods_list')


class PeriodsListView(ListView):
    model = Periods
