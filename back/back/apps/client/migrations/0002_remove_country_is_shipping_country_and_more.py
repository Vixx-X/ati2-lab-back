# Generated by Django 4.0.1 on 2022-07-09 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("client", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="country",
            name="is_shipping_country",
        ),
        migrations.AlterField(
            model_name="social",
            name="client",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="socials",
                to="client.commonclient",
                verbose_name="Client",
            ),
        ),
    ]
