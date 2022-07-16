# Generated by Django 4.0.1 on 2022-07-09 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0002_emaildevice"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="document_id",
        ),
        migrations.AddField(
            model_name="user",
            name="charge",
            field=models.CharField(
                default="ceo", max_length=255, verbose_name="charge"
            ),
            preserve_default=False,
        ),
    ]
