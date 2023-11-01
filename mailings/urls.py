from django.urls import path

from . import views
from .apps import MailingsConfig

app_name = MailingsConfig.name

urlpatterns = [
    path('', views.MailingListView.as_view(), name='mailings_list'),

    path('mailings/create/', views.MailingCreateView.as_view(), name='mailing_create'),
    path('mailings/edit/<int:pk>/', views.MailingUpdateView.as_view(), name='mailing_edit'),

    path('clients/create/', views.ClientCreateView.as_view(), name='client_create'),
    path('clients/', views.ClientListView.as_view(), name='client_list'),

    path('mailings/periods/create/', views.PeriodsCreateView.as_view(), name='periods_create'),
    path('mailings/periods/', views.PeriodsListView.as_view(), name='periods_list'),

    path('messages/', views.MessageListView.as_view(), name='messages_list'),
    path('messages/create', views.MessageCreateView.as_view(), name='messages_create'),

    path('mailing_logs/', views.MailingLogListView.as_view(), name='mailing_log_list'),

]
