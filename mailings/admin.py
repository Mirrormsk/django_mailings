from django.contrib import admin

from .models import Client, Periods


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email')


@admin.register(Periods)
class PeriodsAdmin(admin.ModelAdmin):
    list_display = ('name', 'pattern')
