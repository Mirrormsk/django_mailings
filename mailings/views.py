from django.shortcuts import render
from django.views.generic import ListView

from .models import Mailing


class MailingListView(ListView):
    model = Mailing
