# Generated by Django 2.2.5 on 2020-01-08 05:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('max', '0016_remove_electronics_name_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='electronics',
            name='name_type',
            field=models.ForeignKey(default=11, on_delete=django.db.models.deletion.CASCADE, to='max.Name'),
            preserve_default=False,
        ),
    ]
