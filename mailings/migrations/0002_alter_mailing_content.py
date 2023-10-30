# Generated by Django 4.2.6 on 2023-10-30 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("mailings", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mailing",
            name="content",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                to="mailings.message",
                verbose_name="Содержание",
            ),
        ),
    ]
