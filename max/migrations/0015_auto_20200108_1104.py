# Generated by Django 2.2.5 on 2020-01-08 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('max', '0014_auto_20200108_1102'),
    ]

    operations = [
        migrations.RenameField(
            model_name='electronics',
            old_name='model_type',
            new_name='name_type',
        ),
    ]
