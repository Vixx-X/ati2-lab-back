# Generated by Django 4.0.1 on 2022-07-17 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_remove_user_document_id_user_charge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(error_messages={'unique': 'A user with that username already exists.'}, max_length=254, verbose_name='email address'),
        ),
    ]
