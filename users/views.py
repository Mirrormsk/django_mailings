from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView


class LoginView(BaseLoginView):
    extra_context = {
        'title': 'SkyStore - Вход'
    }


class LogoutView(BaseLogoutView):
    pass
