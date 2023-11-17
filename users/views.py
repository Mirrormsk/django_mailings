from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import get_user_model

from users.forms import UserRegisterForm


class LoginView(BaseLoginView):
    extra_context = {
        'title': 'Сервис рассылок - Вход'
    }


class LogoutView(BaseLogoutView):
    pass


class RegisterView(CreateView):

    model = get_user_model()
    form_class = UserRegisterForm
    success_url = reverse_lazy("users:login")
    template_name = 'users/register.html'

