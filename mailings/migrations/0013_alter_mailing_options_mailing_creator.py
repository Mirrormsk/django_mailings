# Generated by Django 4.2.6 on 2023-11-21 11:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("mailings", "0012_alter_client_note"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="mailing",
            options={
                "permissions": [("can_stop_mailing", "Can stop mailing")],
                "verbose_name": "рассылка",
                "verbose_name_plural": "рассылки",
            },
        ),
        migrations.AddField(
            model_name="mailing",
            name="creator",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="создал",
            ),
            preserve_default=False,
        ),
    ]