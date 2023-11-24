from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand

from blog.models import Article
from mailings.models import Mailing
from users.models import User


class Command(BaseCommand):
    help = "Create groups and assign permissions"

    def handle(self, *args, **options):

        managers_group, managers_created = Group.objects.get_or_create(name='Managers')
        content_managers_group, content_managers_created = Group.objects.get_or_create(name='Content managers')

        mailing_content_type = ContentType.objects.get_for_model(Mailing)
        users_content_type = ContentType.objects.get_for_model(User)
        article_content_type = ContentType.objects.get_for_model(Article)

        view_mailings, _ = Permission.objects.get_or_create(codename='view_mailing',
                                                            content_type=mailing_content_type)
        stop_mailing, _ = Permission.objects.get_or_create(codename='stop_mailing', name='Can stop mailing',
                                                           content_type=mailing_content_type)
        view_users, _ = Permission.objects.get_or_create(codename='view_user',
                                                         content_type=users_content_type)
        block_users, _ = Permission.objects.get_or_create(codename='block_user', name='Can block user',
                                                          content_type=users_content_type)
        add_article, _ = Permission.objects.get_or_create(codename='add_article',
                                                          content_type=article_content_type)
        change_article, _ = Permission.objects.get_or_create(codename='change_article',
                                                             content_type=article_content_type)
        delete_article, _ = Permission.objects.get_or_create(codename='delete_article',
                                                             content_type=article_content_type)

        managers_group.permissions.add(
            view_mailings,
            view_users,
            block_users,
            stop_mailing
        )

        content_managers_group.permissions.add(
            add_article,
            change_article,
            delete_article,
        )

        if managers_created:
            message = 'Managers group were successfully created. Permissions was be added.'
        else:
            message = 'Managers group already exists. Permissions was be updated.'
        self.stdout.write(self.style.SUCCESS(message))

        if content_managers_created:
            message = 'Content managers group were successfully created. Permissions was be added.'
        else:
            message = 'Content managers group already exists. Permissions was be updated.'
        self.stdout.write(self.style.SUCCESS(message))
