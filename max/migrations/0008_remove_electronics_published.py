# Generated by Django 2.2.5 on 2020-01-06 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('max', '0007_auto_20200106_0949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='electronics',
            name='published',
        ),
    ]
