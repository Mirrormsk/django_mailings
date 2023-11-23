from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand

from mailings.models import Mailing
from users.models import User


class Command(BaseCommand):
    help = "Create groups and assign permissions"

    def handle(self, *args, **options):
        managers_group, created = Group.objects.get_or_create(name='Managers')

        mailing_content_type = ContentType.objects.get_for_model(Mailing)
        users_content_type = ContentType.objects.get_for_model(User)

        view_mailings, _ = Permission.objects.get_or_create(codename='view_mailing',
                                                            content_type=mailing_content_type)
        stop_mailing, _ = Permission.objects.get_or_create(codename='stop_mailing', name='Can stop mailing',
                                                           content_type=mailing_content_type)
        view_users, _ = Permission.objects.get_or_create(codename='view_user',
                                                         content_type=users_content_type)
        block_users, _ = Permission.objects.get_or_create(codename='block_user', name='Can block user',
                                                          content_type=users_content_type)

        managers_group.permissions.add(
            view_mailings,
            view_users,
            block_users,
            stop_mailing
        )

        if created:
            message = 'Groups were successfully created. Permissions was be added.'
        else:
            message = 'Group already exists. Permissions was be updated.'

        self.stdout.write(self.style.SUCCESS(message))
