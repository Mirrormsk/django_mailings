# Generated by Django 4.2.6 on 2023-10-31 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("mailings", "0006_remove_periods_pattern_periods_duration"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mailinglog",
            name="client",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="log",
                to="mailings.client",
                verbose_name="получатель",
            ),
        ),
    ]
