# Generated by Django 2.2.5 on 2020-01-06 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('max', '0006_electronics_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='electronics',
            name='published',
            field=models.BooleanField(),
        ),
    ]
