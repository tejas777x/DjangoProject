# Generated by Django 2.2.5 on 2020-01-06 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('max', '0008_remove_electronics_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='electronics',
            name='select',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
