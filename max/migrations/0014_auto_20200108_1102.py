# Generated by Django 2.2.5 on 2020-01-08 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('max', '0013_auto_20200107_2251'),
    ]

    operations = [
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=120)),
            ],
        ),
        migrations.RemoveField(
            model_name='person',
            name='city',
        ),
        migrations.RemoveField(
            model_name='person',
            name='country',
        ),
        migrations.RemoveField(
            model_name='electronics',
            name='item_name',
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.AddField(
            model_name='electronics',
            name='model_type',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='max.Name'),
            preserve_default=False,
        ),
    ]
