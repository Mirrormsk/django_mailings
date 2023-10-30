from django.urls import path

from .apps import MailingsConfig
from .views import MailingListView, ClientCreateView, ClientListView, MailingCreateView, PeriodsCreateView, \
    PeriodsListView, MessageListView, MessageCreateView, MailingUpdateView

app_name = MailingsConfig.name

urlpatterns = [
    path('', MailingListView.as_view(), name='mailings_list'),
    path('mailings/create/', MailingCreateView.as_view(), name='mailing_create'),
    path('mailings/edit/<int:pk>/', MailingUpdateView.as_view(), name='mailing_edit'),
    path('clients/create/', ClientCreateView.as_view(), name='client_create'),
    path('mailings/periods/create/', PeriodsCreateView.as_view(), name='periods_create'),
    path('mailings/periods/', PeriodsListView.as_view(), name='periods_list'),
    path('clients/', ClientListView.as_view(), name='client_list'),
    path('messages/', MessageListView.as_view(), name='messages_list'),
    path('messages/create', MessageCreateView.as_view(), name='messages_create'),

]
