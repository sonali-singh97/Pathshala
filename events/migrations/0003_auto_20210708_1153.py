# Generated by Django 3.2.2 on 2021-07-08 11:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20210705_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='day',
        ),
        migrations.RemoveField(
            model_name='event',
            name='month',
        ),
        migrations.RemoveField(
            model_name='event',
            name='year',
        ),
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]