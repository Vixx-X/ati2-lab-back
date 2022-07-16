# Generated by Django 4.0.1 on 2022-07-13 01:45

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ("client", "0002_remove_country_is_shipping_country_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="address",
            options={"verbose_name": "Address", "verbose_name_plural": "Addresses"},
        ),
        migrations.RemoveField(
            model_name="particularclient",
            name="whatsapp",
        ),
        migrations.AddField(
            model_name="client",
            name="whatsapp",
            field=phonenumber_field.modelfields.PhoneNumberField(
                blank=True, max_length=128, region=None, verbose_name="whatsapp"
            ),
        ),
        migrations.AlterField(
            model_name="address",
            name="client",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="addresses",
                to="client.commonclient",
                verbose_name="Client",
            ),
        ),
    ]
