from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from users import texts


def send_verify_mail(form, request):
    user = form.save(commit=False)
    user.is_active = False
    user.save()
    current_site = get_current_site(request)
    mail_subject = texts.register_mail_subject.format(current_site)
    token = default_token_generator.make_token(user)
    to_email = form.cleaned_data.get("email")

    message = render_to_string(
        "users/email_templates/confirm_email_message.html",
        {
            "user": user,
            "current_site": current_site,
            "domain": current_site.domain,
            "uid": user.uid,
            "token": token,
        },
    )

    activation_email = EmailMessage(subject=mail_subject, body=message, to=[to_email])

    activation_email.content_subtype = "html"
    activation_email.send()
