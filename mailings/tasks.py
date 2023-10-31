from .services import MailService


mail_service = MailService()


def check_mailing_list():
    mail_service.process_mailing_list()
