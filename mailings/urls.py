from django.urls import path

from .views import MailingListView
from .apps import MailingsConfig

app_name = MailingsConfig.name

urlpatterns = [
    path('', MailingListView.as_view(), name='mailings_list')
]
