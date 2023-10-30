# Generated by Django 4.2.6 on 2023-10-30 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("mailings", "0002_alter_mailing_content"),
    ]

    operations = [
        migrations.CreateModel(
            name="MailingLog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("time", models.DateTimeField(auto_now_add=True, verbose_name="время")),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("success", "Доставлено"),
                            ("fail", "Не доставлено"),
                            ("error", "Ошибка"),
                        ],
                        max_length=20,
                        verbose_name="статус",
                    ),
                ),
                (
                    "error_message",
                    models.CharField(
                        blank=True,
                        max_length=250,
                        null=True,
                        verbose_name="Текст ошибки",
                    ),
                ),
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mailings.client",
                        verbose_name="получатель",
                    ),
                ),
                (
                    "mailing",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mailings.mailing",
                        verbose_name="рассылка",
                    ),
                ),
            ],
        ),
    ]