# Generated by Django 4.2.6 on 2023-11-01 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("mailings", "0010_delete_message"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mailing",
            name="audience",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="mailings.audience",
                verbose_name="аудитория",
            ),
        ),
    ]
