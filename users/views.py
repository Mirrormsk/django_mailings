from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users import texts
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

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        current_site = get_current_site(self.request)
        mail_subject = texts.register_mail_subject.format(current_site)
        token = default_token_generator.make_token(user)
        to_email = form.cleaned_data.get('email')

        message = render_to_string('users/email_templates/confirm_email_message.html',
                                   {
                                       'user': user,
                                       'current_site': current_site,
                                       'domain': current_site.domain,
                                       'uid': user.uid,
                                       'token': token,
                                   })

        activation_email = EmailMessage(
            subject=mail_subject,
            body=message,
            to=[to_email]
        )

        activation_email.content_subtype = "html"
        activation_email.send()
        return HttpResponse('Ссылка для подтверждения отправлена на ваш email.')


def activate_user(request, uid, token):
    UserModel: AbstractUser = get_user_model()
    try:
        user = UserModel.objects.get(uid=uid)
    except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Спасибо за регистрацию! Теперь вы можете войти в свой аккаунт')

    return HttpResponse('Неверная ссылка активации!')
