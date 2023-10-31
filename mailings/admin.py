from django.contrib import admin

from .models import Client, Periods, Mailing, Audience


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email')


@admin.register(Periods)
class PeriodsAdmin(admin.ModelAdmin):
    list_display = ('name', 'pattern')


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('name', )