from datetime import datetime
from smtplib import SMTPException

from django.core.mail import send_mail

from config.settings import DEFAULT_FROM_EMAIL
from .models import Mailing, Client, MailingLog


class MailService:

    @staticmethod
    def get_mailings():
        return Mailing.objects.filter(status=Mailing.STATUS_STARTED)

    @staticmethod
    def send_one_email(mailing: Mailing, recipient: Client):
        try:
            result = send_mail(
                subject=mailing.content.title,
                from_email=DEFAULT_FROM_EMAIL,
                message=mailing.content.body,
                recipient_list=[recipient.email],
            )
        except SMTPException as ex:
            error_message = ex
            status = MailingLog.STATUS_ERROR
        else:
            error_message = None
            status = MailingLog.STATUS_SUCCESS if result else MailingLog.STATUS_FAILED
        finally:
            log_obj = MailingLog(
                client=recipient,
                mailing=mailing,
                status=status,
                error_message=error_message,
            )
            log_obj.save()

    def process_mailing(self, mailing: Mailing):
        recipients = Mailing.audience.recipients.all()
        for recipient in recipients:
            self.send_one_email(mailing, recipient)

    def process_mailing_list(self):
        mailings = self.get_mailings()
        now = datetime.now()

        for mailing in mailings:
            if now >= mailing.start_time:
                self.process_mailing(mailing)

