# Generated by Django 2.2.5 on 2020-01-07 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('max', '0010_auto_20200106_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='electronics',
            name='select',
            field=models.BooleanField(),
        ),
    ]
