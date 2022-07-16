# Generated by Django 4.0.1 on 2022-07-16 22:10

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ("business", "0005_commonbusiness_website_alter_commonbusiness_tax_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="employee",
            name="local_phone_number",
            field=phonenumber_field.modelfields.PhoneNumberField(
                blank=True,
                max_length=128,
                region=None,
                verbose_name="local phone number",
            ),
        ),
    ]