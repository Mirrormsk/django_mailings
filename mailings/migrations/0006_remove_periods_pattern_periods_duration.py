# Generated by Django 4.2.6 on 2023-10-31 10:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mailings", "0005_remove_mailing_recipients_alter_mailing_content_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="periods",
            name="pattern",
        ),
        migrations.AddField(
            model_name="periods",
            name="duration",
            field=models.DurationField(
                default=datetime.timedelta(days=7),
                unique=True,
                verbose_name="Повторять каждые",
            ),
        ),
    ]
